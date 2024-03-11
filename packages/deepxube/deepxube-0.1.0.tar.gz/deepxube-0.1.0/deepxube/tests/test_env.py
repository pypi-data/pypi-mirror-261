from typing import List

import torch
import torch.nn as nn
from torch.multiprocessing import Queue, get_context

from deepxube.environments.environment_abstract import Environment, State
from deepxube.utils import nnet_utils
import numpy as np

import time


def data_runner(queue1: Queue, queue2: Queue):
    while True:
        the = queue1.get()
        if the is None:
            break
        queue2.put(the)


def test_env(env: Environment, num_states: int, step_max: int):
    torch.set_num_threads(1)

    # generate start/goal states
    start_time = time.time()
    states = env.get_start_states(num_states)

    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Generated %i start states in %s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    # get data
    start_time = time.time()
    states: List[State]
    states, goals = env.get_start_goal_pairs(list(np.random.randint(step_max, size=num_states)))

    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Generated %i start/goal states in %s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    # expand
    start_time = time.time()
    env.expand(states)
    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Expanded %i states in %s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    # nnet format
    start_time = time.time()
    states_nnet = env.states_to_nnet_input(states)
    elapsed_time = time.time() - start_time
    states_per_sec = len(states) / elapsed_time
    print("Converted %i states to nnet format in "
          "%s seconds (%.2f/second)" % (len(states), elapsed_time, states_per_sec))

    start_time = time.time()
    goals_nnet = env.goals_to_nnet_input(goals)
    elapsed_time = time.time() - start_time
    states_per_sec = len(goals) / elapsed_time
    print("Converted %i goals to nnet format in "
          "%s seconds (%.2f/second)" % (len(goals), elapsed_time, states_per_sec))

    # get heuristic fn
    on_gpu: bool
    device: torch.device
    device, devices, on_gpu = nnet_utils.get_device()
    print("device: %s, devices: %s, on_gpu: %s" % (device, devices, on_gpu))

    nnet: nn.Module = env.get_v_nnet()
    nnet.to(device)
    if on_gpu:
        nnet = nn.DataParallel(nnet)

    # initialize nnet
    print("")
    heuristic_fn = nnet_utils.get_heuristic_fn(nnet, device, env)
    heuristic_fn(states_nnet, goals_nnet, is_nnet_format=True)

    # nnet heuristic
    start_time = time.time()
    heuristic_fn(states_nnet, goals_nnet, is_nnet_format=True)

    nnet_time = time.time() - start_time
    states_per_sec = len(states) / nnet_time
    print("Computed heuristic for %i states in %s seconds (%.2f/second)" % (len(states), nnet_time, states_per_sec))

    # multiprocessing
    print("")
    start_time = time.time()
    ctx = get_context("spawn")
    queue1: ctx.Queue = ctx.Queue()
    queue2: ctx.Queue = ctx.Queue()
    proc = ctx.Process(target=data_runner, args=(queue1, queue2))
    proc.daemon = True
    proc.start()
    print("Process start time: %.2f" % (time.time() - start_time))

    queue1.put((states_nnet, goals_nnet))
    queue2.get()

    start_time = time.time()
    queue1.put((states, goals))
    print("State/goals send time: %s" % (time.time() - start_time))

    start_time = time.time()
    queue2.get()
    print("States/goals get time: %.2f" % (time.time() - start_time))

    start_time = time.time()
    queue1.put((states_nnet, goals_nnet))
    print("State/goals nnet send time: %s" % (time.time() - start_time))

    start_time = time.time()
    queue2.get()
    print("States/goals nnet get time: %.2f" % (time.time() - start_time))

    start_time = time.time()
    queue1.put(env)
    print("Environment send time: %s" % (time.time() - start_time))

    start_time = time.time()
    queue2.get()
    print("Environment get time: %s" % (time.time() - start_time))

    start_time = time.time()
    queue1.put(None)
    proc.join()
    print("Process join time: %.2f" % (time.time() - start_time))
