from typing import Tuple, List, Set, Union, cast, Dict, Optional

import torch
from torch import Tensor, nn

from deepxube.utils import misc_utils
from deepxube.utils.pytorch_models import FullyConnectedModel, ResnetModel, Conv2dModel

import numpy as np
import matplotlib.pyplot as plt
from deepxube.environments.environment_abstract import EnvGrndAtoms, State, HeurFnNNet, Goal
from deepxube.logic.program import Atom, Model

import pickle

import re

import pathlib
import tarfile
import os
import wget
from filelock import FileLock


class NNet(HeurFnNNet):
    def __init__(self, h1_dim: int, resnet_dim: int, num_resnet_blocks: int, out_dim: int, batch_norm: bool,
                 nnet_type: str):
        super().__init__(nnet_type)
        # self.img_nnet = Conv2dModel(3, [16, 16], [2, 2], [0, 0], [True, True], ["RELU", "RELU"], strides=[2, 2])

        self.conv_to_flat = nn.Sequential(
            Conv2dModel(6, [16, 16], [2, 2], [1, 0], [True, True], ["RELU", "RELU"], strides=[1, 1]),
            nn.Flatten(),
        )

        self.first_fc = FullyConnectedModel(1600, [h1_dim, resnet_dim], [batch_norm] * 2, ["RELU"] * 2)
        self.resnet = ResnetModel(resnet_dim, num_resnet_blocks, out_dim, batch_norm, layer_act="RELU")

    def forward(self, states_l: List[Tensor], goals_l: List[Tensor]):
        # img_nnet_out: Tensor = self.img_nnet(states_l[0])
        x = self.conv_to_flat(torch.cat((states_l[0], goals_l[0]), dim=1).float())
        x = self.first_fc(x)
        x = self.resnet(x)

        return x


class SokobanState(State):
    __slots__ = ['agent', 'walls', 'boxes', 'hash']

    def __init__(self, agent: np.array, boxes: np.ndarray, walls: np.ndarray):
        self.agent: np.array = agent
        self.boxes: np.ndarray = boxes
        self.walls: np.ndarray = walls

        self.hash = None

    def __hash__(self):
        if self.hash is None:
            boxes_flat = self.boxes.flatten()
            walls_flat = self.walls.flatten()
            state = np.concatenate((self.agent, boxes_flat, walls_flat), axis=0)

            self.hash = hash(state.tobytes())

        return self.hash

    def __eq__(self, other: 'SokobanState'):
        agents_eq: bool = np.array_equal(self.agent, other.agent)
        boxes_eq: bool = np.array_equal(self.boxes, other.boxes)
        walls_eq: bool = np.array_equal(self.walls, other.walls)

        return agents_eq and boxes_eq and walls_eq


class SokobanGoal(Goal):
    __slots__ = ['agent', 'walls', 'boxes']

    def __init__(self, agent: np.array, boxes: np.ndarray, walls: np.ndarray):
        self.agent: np.array = agent
        self.boxes: np.ndarray = boxes
        self.walls: np.ndarray = walls


def load_states(file_name: str) -> List[SokobanState]:
    # states_np = pickle.load(open(file_name, "rb"))
    t_file = tarfile.open(file_name, "r:gz")
    states_np = pickle.load(t_file.extractfile(t_file.getmembers()[1]))

    states: List[SokobanState] = []

    agent_idxs = np.where(states_np == 1)
    box_masks = states_np == 2
    wall_masks = states_np == 4

    for idx in range(states_np.shape[0]):
        agent_idx = np.array([agent_idxs[1][idx], agent_idxs[2][idx]], dtype=int)

        states.append(SokobanState(agent_idx, box_masks[idx], wall_masks[idx]))

    return states


def _get_surfaces():
    import imageio.v2 as imageio
    parent_dir: str = str(pathlib.Path(__file__).parent.resolve())
    img_dir = f"{parent_dir}/data/sokoban/"

    lock = FileLock(f"{parent_dir}/data/sokoban/file.lock")
    with lock:
        # Load images, representing the corresponding situation
        box = imageio.imread(f"{img_dir}/surface/box.png")
        # box_on_target = imageio.imread(f"{img_dir}/surface/box_on_target.png")
        # box_target = imageio.imread(f"{img_dir}/surface/box_target.png")
        floor = imageio.imread(f"{img_dir}/surface/floor.png")
        player = imageio.imread(f"{img_dir}/surface/player.png")
        # player_on_target = imageio.imread(f"{img_dir}/surface/player_on_target.png")
        wall = imageio.imread(f"{img_dir}/surface/wall.png")

    # surfaces = [wall, floor, box_target, player, box, player_on_target, box_on_target]
    surfaces = [wall, floor, player, box]

    return surfaces


def _get_train_states() -> List[SokobanState]:
    data_dir, data_file = get_data_dir_and_file_name()
    lock = FileLock(f"{data_dir}/file.lock")

    with lock:
        states_train: List[SokobanState] = load_states(data_file)

    return states_train


def _np_to_model(agent: np.array, boxes: np.ndarray, walls: np.ndarray) -> Model:
    grnd_atoms: List[Atom] = []
    if agent.shape[0] > 0:
        grnd_atoms += [('agent', str(int(agent[0])), str(int(agent[1])))]
    grnd_atoms += [('box', str(int(x)), str(int(y))) for x, y in zip(*np.where(boxes))]
    grnd_atoms += [('wall', str(int(x)), str(int(y))) for x, y in zip(*np.where(walls))]

    return frozenset(grnd_atoms)


def get_data_dir_and_file_name() -> Tuple[str, str]:
    parent_dir: str = str(pathlib.Path(__file__).parent.resolve())
    data_dir: str = f"{parent_dir}/data/sokoban/"
    file_name: str = f"{data_dir}/sokoban.tar.gz"

    return data_dir, file_name


class Sokoban(EnvGrndAtoms):

    def __init__(self, env_name: str):
        super().__init__(env_name)

        self.dim: int = 10
        self.num_boxes: int = 4

        self.num_actions: int = 4

        self.img_dim: int = 160

        self.states_train: Optional[List[SokobanState]] = None
        self._surfaces = None

        # check if data needs to be downloaded
        data_dir, file_name = get_data_dir_and_file_name()
        data_download_link: str = "https://github.com/forestagostinelli/DeepXubeData/raw/main/sokoban.tar.gz"
        if not os.path.exists(file_name):
            valid_user_in: bool = False
            while not valid_user_in:
                user_in: str = input(f"Sokoban data needs to be downloaded from {data_download_link}. "
                                     f"Download data (about 16MB)? (y/n):")
                if user_in.upper() == "Y":
                    valid_user_in = True
                    if not os.path.exists(data_dir):
                        os.makedirs(data_dir)
                    wget.download(data_download_link, file_name, bar=None)
                elif user_in.upper() == "N":
                    valid_user_in = True

    def next_state(self, states: List[SokobanState], actions: List[int]) -> Tuple[List[SokobanState], List[float]]:
        agent = np.stack([state.agent for state in states], axis=0)
        boxes = np.stack([state.boxes for state in states], axis=0)
        walls_next = np.stack([state.walls for state in states], axis=0)

        idxs_arange = np.arange(0, len(states))
        agent_next_tmp = self._get_next_idx(agent, actions)
        agent_next = np.zeros(agent_next_tmp.shape, dtype=int)

        boxes_next = boxes.copy()

        # agent -> wall
        agent_wall = walls_next[idxs_arange, agent_next_tmp[:, 0], agent_next_tmp[:, 1]]
        agent_next[agent_wall] = agent[agent_wall]

        # agent -> box
        agent_box = boxes[idxs_arange, agent_next_tmp[:, 0], agent_next_tmp[:, 1]]
        boxes_next_tmp = self._get_next_idx(agent_next_tmp, actions)

        box_wall = walls_next[idxs_arange, boxes_next_tmp[:, 0], boxes_next_tmp[:, 1]]
        box_box = boxes[idxs_arange, boxes_next_tmp[:, 0], boxes_next_tmp[:, 1]]

        # agent -> box -> obstacle
        agent_box_obstacle = agent_box & (box_wall | box_box)
        agent_next[agent_box_obstacle] = agent[agent_box_obstacle]

        # agent -> box -> empty
        agent_box_empty = agent_box & np.logical_not(box_wall | box_box)
        agent_next[agent_box_empty] = agent_next_tmp[agent_box_empty]
        abe_idxs = np.where(agent_box_empty)[0]

        agent_next_idxs_abe = agent_next[agent_box_empty]
        boxes_next_idxs_abe = boxes_next_tmp[agent_box_empty]

        boxes_next[abe_idxs, agent_next_idxs_abe[:, 0], agent_next_idxs_abe[:, 1]] = False
        boxes_next[abe_idxs, boxes_next_idxs_abe[:, 0], boxes_next_idxs_abe[:, 1]] = True

        # agent -> empty
        agent_empty = np.logical_not(agent_wall | agent_box)
        agent_next[agent_empty] = agent_next_tmp[agent_empty]
        boxes_next[agent_empty] = boxes[agent_empty]

        states_next: List[SokobanState] = []
        for idx in range(len(states)):
            state_next: SokobanState = SokobanState(agent_next[idx], boxes_next[idx], walls_next[idx])
            states_next.append(state_next)

        transition_costs: List[int] = [1 for _ in range(len(states))]

        return states_next, transition_costs

    def get_state_actions(self, states: List[SokobanState]) -> List[List[int]]:
        return [list(range(self.num_actions)) for _ in range(len(states))]

    def is_solved(self, states: List[SokobanState], goals: List[SokobanGoal]) -> List[bool]:
        states_np: np.ndarray = self.states_to_nnet_input(states)[0].reshape((len(states), -1))
        goals_np: np.ndarray = self.goals_to_nnet_input(goals)[0].reshape((len(goals), -1))
        is_solved_np = np.all(np.logical_or(states_np == goals_np, goals_np == 0), axis=1)
        return list(is_solved_np)

    def get_start_states(self, num_states: int) -> List[SokobanState]:
        if self.states_train is None:
            self.states_train = _get_train_states()
        state_idxs = np.random.randint(0, len(self.states_train), size=num_states)
        states: List[SokobanState] = [self.states_train[idx] for idx in state_idxs]

        step_range: Tuple[int, int] = (0, 100)

        # Initialize
        scrambs: List[int] = list(range(step_range[0], step_range[1] + 1))

        # Scrambles
        step_nums: np.array = np.random.choice(scrambs, num_states)
        step_nums_curr: np.array = np.zeros(num_states)

        # Go backward from goal state
        steps_lt = step_nums_curr < step_nums
        while np.any(steps_lt):
            idxs: np.ndarray = np.where(steps_lt)[0]

            states_to_move: List[SokobanState] = [states[idx] for idx in idxs]
            actions = list(np.random.randint(0, self.num_actions, size=len(states_to_move)))

            states_moved, _ = self.next_state(states_to_move, actions)

            for idx_moved, idx in enumerate(idxs):
                states[idx] = states_moved[idx_moved]

            step_nums_curr[idxs] = step_nums_curr[idxs] + 1
            steps_lt[idxs] = step_nums_curr[idxs] < step_nums[idxs]

        return states

    def states_to_nnet_input(self, states: List[SokobanState]) -> List[np.ndarray]:
        """
        states_real: np.ndarray = np.zeros((len(states), self.img_dim, self.img_dim, 3))
        for state_idx, state in enumerate(states):
            states_real[state_idx] = self.state_to_rgb(state)

        states_rep = [states_real.transpose([0, 3, 1, 2])]
        """

        states_rep_np: np.ndarray = np.zeros((len(states), 3, self.dim, self.dim), dtype=np.uint8)
        for idx, state in enumerate(states):
            states_rep_np[idx, 0, state.agent[0], state.agent[1]] = 1
            states_rep_np[idx, 1, :, :] = state.boxes
            states_rep_np[idx, 2, :, :] = state.walls
        states_rep = [states_rep_np]

        return states_rep

    def goals_to_nnet_input(self, goals: List[SokobanGoal]) -> List[np.ndarray]:
        states_rep_np: np.ndarray = np.zeros((len(goals), 3, self.dim, self.dim), dtype=np.uint8)
        for idx, goal in enumerate(goals):
            if goal.agent.shape[0] > 0:
                states_rep_np[idx, 0, goal.agent[0], goal.agent[1]] = 1
            states_rep_np[idx, 1, :, :] = goal.boxes
            states_rep_np[idx, 2, :, :] = goal.walls
        states_rep = [states_rep_np]

        return states_rep

    def state_to_model(self, states: List[SokobanState]) -> List[Model]:
        agents_np = np.stack([state.agent for state in states], axis=0)
        boxes_np = np.stack([state.boxes for state in states], axis=0)
        walls_np = np.stack([state.walls for state in states], axis=0)

        models_s: List[Model] = []
        for agent_i, boxes_i, walls_i in zip(agents_np, boxes_np, walls_np):
            models_s.append(_np_to_model(agent_i, boxes_i, walls_i))

        return models_s

    def model_to_state(self, models: List[Model]) -> List[State]:
        raise NotImplementedError

    def goal_to_model(self, goals: List[SokobanGoal]) -> List[Model]:
        agent = np.stack([goal.agent for goal in goals], axis=0)
        boxes = np.stack([goal.boxes for goal in goals], axis=0)
        walls = np.stack([goal.walls for goal in goals], axis=0)

        models_s: List[Model] = []
        for agent_i, boxes_i, walls_i in zip(agent, boxes, walls):
            models_s.append(_np_to_model(agent_i, boxes_i, walls_i))

        return models_s

    def model_to_goal(self, models: List[Model]) -> List[SokobanGoal]:
        models_np = self._models_to_np(models)
        goals: List[SokobanGoal] = []
        for i in range(len(models)):
            agent_idxs = np.concatenate(np.where(models_np[i, 0]))
            goals.append(SokobanGoal(agent_idxs, models_np[i, 1], models_np[i, 2]))

        return goals

    def get_pddl_domain(self) -> List[str]:
        pddl_str: str = """
        (define (domain sokoban)
  (:requirements :typing )
  (:types thing location direction)
  (:predicates (move-dir ?v0 - location ?v1 - location ?v2 - direction)
    (is-nongoal ?v0 - location)
    (clear ?v0 - location)
    (is-stone ?v0 - thing)
    (at ?v0 - thing ?v1 - location)
    (is-player ?v0 - thing)
    (at-goal ?v0 - thing)
    (move ?v0 - direction)
    (is-goal ?v0 - location)
  )

    (:action move
    :parameters (?p - thing ?from - location ?to - location ?dir - direction)
    :precondition (and (move ?dir)
        (is-player ?p)
        (at ?p ?from)
        (clear ?to)
        (move-dir ?from ?to ?dir))
    :effect (and
        (not (at ?p ?from))
        (not (clear ?to))
        (at ?p ?to)
        (clear ?from))
)

(:action push-to-goal
    :parameters (?p - thing ?s - thing ?ppos - location ?from - location ?to - location ?dir - direction)
    :precondition (and (move ?dir)
        (is-player ?p)
        (is-stone ?s)
        (at ?p ?ppos)
        (at ?s ?from)
        (clear ?to)
        (move-dir ?ppos ?from ?dir)
        (move-dir ?from ?to ?dir)
        (is-goal ?to))
    :effect (and
        (not (at ?p ?ppos))
        (not (at ?s ?from))
        (not (clear ?to))
        (at ?p ?from)
        (at ?s ?to)
        (clear ?ppos)
        (at-goal ?s))
)


(:action push-to-nongoal
    :parameters (?p - thing ?s - thing ?ppos - location ?from - location ?to - location ?dir - direction)
    :precondition (and (move ?dir)
        (is-player ?p)
        (is-stone ?s)
        (at ?p ?ppos)
        (at ?s ?from)
        (clear ?to)
        (move-dir ?ppos ?from ?dir)
        (move-dir ?from ?to ?dir)
        (is-nongoal ?to))
    :effect (and
        (not (at ?p ?ppos))
        (not (at ?s ?from))
        (not (clear ?to))
        (at ?p ?from)
        (at ?s ?to)
        (clear ?ppos)
        (not (at-goal ?s)))
)
)
       """
        return pddl_str.split("\n")

    def state_goal_to_pddl_inst(self, state: SokobanState, goal: SokobanGoal) -> List[str]:
        model: Model = self.goal_to_model([goal])[0]
        inst_l: List[str] = ["(define(problem sokobaninst)", "(:domain sokoban)"]
        dir_objects: List[str] = ["dir-down - direction", "dir-up - direction", "dir-left - direction",
                                  "dir-right - direction"]
        box_objects: List[str] = [f"stone-{i} - thing" for i in range(self.num_boxes)]
        pos_objects: List[str] = []
        for idx1 in range(self.dim):
            for idx2 in range(self.dim):
                pos_objects.append(f"pos-{idx1}-{idx2} - location")
        inst_l.append("(:objects")
        for obj in dir_objects + pos_objects + ["player-1 - thing "] + box_objects:
            inst_l.append(obj)
        inst_l.append(")")

        inst_l.append("(:init")
        inst_l.append(f"(at player-1 pos-{state.agent[0]}-{state.agent[1]})")
        idxs1, idxs2 = np.where(state.boxes)
        for box_idx, (idx1, idx2) in enumerate(zip(list(idxs1), list(idxs2))):
            inst_l.append(f"(at stone-{box_idx} pos-{idx1}-{idx2})")

        states_np = self.states_to_nnet_input([state])[0][0]
        states_np_any = states_np.any(axis=0)
        for idx1 in range(self.dim):
            for idx2 in range(self.dim):
                if states_np_any[idx1, idx2] == 0:
                    inst_l.append(f"(clear pos-{idx1}-{idx2})")

        goal_boxes_np: np.ndarray = self._models_to_np([model])[0][1]
        for idx1 in range(self.dim):
            for idx2 in range(self.dim):
                if goal_boxes_np[idx1, idx2] == 1:
                    inst_l.append(f"(is-goal pos-{idx1}-{idx2})")
                else:
                    inst_l.append(f"(is-nongoal pos-{idx1}-{idx2})")

        inst_l.append("(is-player player-1)")
        for box_idx in range(self.num_boxes):
            inst_l.append(f"(is-stone stone-{box_idx})")
        inst_l.append("(move dir-down) (move dir-up) (move dir-right) (move dir-left)")

        for action, act_name in zip([0, 1, 2, 3], ["left", "right", "down", "up"]):
            for idx1 in range(self.dim):
                for idx2 in range(self.dim):
                    curr_idxs = np.array([[idx1, idx2]])
                    next_idxs = self._get_next_idx(curr_idxs, [action])[0]
                    if np.all(curr_idxs[0] == next_idxs):
                        continue
                    inst_l.append(f"(move-dir pos-{idx1}-{idx2} pos-{next_idxs[0]}-{next_idxs[1]} dir-{act_name})")
        inst_l.append(")")

        inst_l.append("(:goal")
        inst_l.append("(and")
        for box_idx in range(self.num_boxes):
            inst_l.append(f"(at-goal stone-{box_idx})")
        inst_l.append(")")
        inst_l.append(")")

        inst_l.append(")")
        return inst_l

    def pddl_action_to_action(self, pddl_action: str) -> int:
        str_to_act: Dict[str, int] = {"left": 0, "right": 1, "down": 2, "up": 3}
        act_str: str = re.search(".*dir-(\S+).*", pddl_action).group(1)
        return str_to_act[act_str]

    def get_v_nnet(self) -> nn.Module:
        nnet = NNet(5000, 1000, 4, 1, True, "V")
        return nnet

    def get_q_nnet(self) -> nn.Module:
        nnet = NNet(5000, 1000, 4, 4, True, "Q")
        return nnet

    def start_state_fixed(self, states: List[SokobanState]) -> List[Model]:
        models: List[Model] = self.state_to_model(states)
        fixed_l: List[Model] = []
        for model in models:
            fixed_atoms: List[Atom] = []
            for atom in model:
                if atom[0] == 'wall':
                    fixed_atoms.append(atom)

            fixed_l.append(frozenset(fixed_atoms))
        return fixed_l

    def get_ground_atoms(self) -> List[str]:
        return ["{ agent(X,Y) : pos_x(X), pos_y(Y) } 1",
                "{ box(X,Y) : pos_x(X), pos_y(Y) } %i" % self.num_boxes]

    def on_model(self, m) -> Model:
        symbs: Set = set(str(x) for x in m.symbols(shown=True))
        atoms: List[Atom] = []
        for symb in symbs:
            symb = misc_utils.remove_all_whitespace(symb)

            match = re.search("agent\((\S+),(\S+)\)", symb)
            if match is not None:
                atom: Atom = ("agent", match.group(1), match.group(2))
                atoms.append(atom)

            match = re.search("box\((\S+),(\S+)\)", symb)
            if match is not None:
                atom: Atom = ("box", match.group(1), match.group(2))
                atoms.append(atom)

            match = re.search("wall\((\S+),(\S+)\)", symb)
            if match is not None:
                atom: Atom = ("wall", match.group(1), match.group(2))
                atoms.append(atom)

        model: Model = frozenset(atoms)
        return model

    def get_bk(self) -> List[str]:
        bk: List[str] = ["pos_x(0..9).", "pos_y(0..9).", "pos_min_x(0).", "pos_max_x(9).", "pos_min_y(0).",
                         "pos_max_y(9).", "at_edge_x(X) :- pos_min_x(X).", "at_edge_x(X) :- pos_max_x(X).",
                         "at_edge_y(X) :- pos_min_y(X).", "at_edge_y(X) :- pos_max_y(X).",
                         "validpos2(X,Y,Xr,Yr) :- pos_x(X), pos_y(Y), pos_x(Xr), pos_y(Yr)."]

        bk.extend([
            "\ndir(up).", "dir(down).", "dir(left).", "dir(right).",
            "manhat(up).", "manhat(down).", "manhat(left).", "manhat(right).",
            "\nadj(up,right).", "adj(up,left).", "adj(down,right).", "adj(down,left).", "adj(X,Y) :- adj(Y,X).",
            "opp(up,down).", "opp(left,right).", "opp(X,Y) :- opp(Y,X).",
            "%empty(X,Y) :- pos_x(X), pos_y(Y), not agent(X,Y), not box(X,Y), not wall(X,Y).",

            "\nrel(X,Y,Xr,Y,up) :- validpos2(X,Y,Xr,Y), Xr=X+1.",
            "rel(X,Y,Xr,Y,down) :- validpos2(X,Y,Xr,Y), Xr=X-1.",
            "rel(X,Y,X,Yr,left) :- validpos2(X,Y,X,Yr), Yr=Y-1.",
            "rel(X,Y,X,Yr,right) :- validpos2(X,Y,X,Yr), Yr=Y+1.",

            "\nimmovable(X,Y) :- wall(X,Y).",
            "immovable(X,Y) :- box_stuck(X,Y).",
            "at_edge_d(X,Y,up) :- pos_max_x(X), pos_y(Y).",
            "at_edge_d(X,Y,down) :- pos_min_x(X), pos_y(Y).",
            "at_edge_d(X,Y,left) :- pos_x(X), pos_min_y(Y).",
            "at_edge_d(X,Y,right) :- pos_x(X), pos_max_y(Y).",
            "immovable_edge_d(X,Y,D) :- rel(X,Y,Xr,Yr,D), immovable(Xr,Yr).",
            "immovable_edge_d(X,Y,D) :- at_edge_d(X,Y,D).",

            "\nbox_stuck(X,Y) :- box(X,Y), manhat(D1), immovable_edge_d(X,Y,D1), adj(D1,D2), "
            "immovable_edge_d(X,Y,D2).",

            "\nbox_of_boxes :- box(X,Y), box(X+1,Y), box(X,Y-1), box(X+1,Y-1).",
            "\nagent_box_corners :- agent(X,Y), box(X+1,Y+1), box(X+1,Y-1), box(X-1,Y+1), box(X-1,Y-1).",

            "\n% contraints",
            ":- box(X,Y), wall(X,Y).",
            ":- box(X,Y), agent(X,Y).",
            ":- wall(X,Y), agent(X,Y).",
        ])
        """
        bk.extend([
            "adj(O1,O2) :- at(O1,X1,Y1), at(O2,X2,Y2), adj(X1,Y1,X2,Y2).",
            "box_stuck(B) :- #count{Obj: adj(B, Obj), immovable(Obj)} >= 2.",
        ])
        """

        return bk

    def get_render_array(self, state: Union[SokobanState, Model]) -> np.ndarray:
        state_rendered = np.ones((self.dim, self.dim), dtype=int)
        if type(state) is SokobanState:
            state_rendered -= state.walls
            state_rendered[state.agent[0], state.agent[1]] = 2
            state_rendered += state.boxes * 2
        else:
            state: Model = cast(Model, state)
            model_np = self._models_to_np([state])[0]
            state_rendered -= model_np[2]
            state_rendered = state_rendered * (1 - model_np[0]) + 2 * model_np[0]
            state_rendered += model_np[1] * 2

        """
        state_rendered += (state.boxes & state.goals) * 5
        state_rendered += (state.boxes & np.logical_not(state.goals)) * 3

        state_rendered += (state.goals & np.logical_not(state.boxes)) * 1

        if state.goals[state.agent[0], state.agent[1]]:
            state_rendered[state.agent[0], state.agent[1]] = 5
        else:
            state_rendered[state.agent[0], state.agent[1]] = 3
        """

        return state_rendered

    def visualize(self, states: Union[List[SokobanState], List[Model]]) -> np.ndarray:
        states_img: np.ndarray = np.zeros((len(states), self.img_dim, self.img_dim, 3))

        import cv2
        if self._surfaces is None:
            self._surfaces = _get_surfaces()

        for state_idx, state in enumerate(states):
            room = self.get_render_array(state)

            # Assemble the new rgb_room, with all loaded images
            room_rgb = np.zeros(shape=(room.shape[0] * 16, room.shape[1] * 16, 3), dtype=np.uint8)
            for i in range(room.shape[0]):
                x_i = i * 16

                for j in range(room.shape[1]):
                    y_j = j * 16
                    surfaces_id = room[i, j]

                    room_rgb[x_i:(x_i + 16), y_j:(y_j + 16), :] = self._surfaces[surfaces_id]

            room_rgb = room_rgb / 255

            states_img[state_idx] = cv2.resize(room_rgb, (self.img_dim, self.img_dim))

        return states_img

    def _models_to_np(self, models: List[Model]) -> np.ndarray:
        goals_rep: np.ndarray = np.zeros((len(models), 3, self.dim, self.dim), np.uint8)
        for idx, model in enumerate(models):
            agent_idx = np.array([atom[1:] for atom in model if atom[0] == "agent"]).astype(int)
            box_idxs = np.array([atom[1:] for atom in model if atom[0] == "box"]).astype(int)
            wall_idxs = np.array([atom[1:] for atom in model if atom[0] == "wall"]).astype(int)

            if agent_idx.shape[0] > 0:
                goals_rep[idx, 0, agent_idx[:, 0], agent_idx[:, 1]] = 1
            if box_idxs.shape[0] > 0:
                goals_rep[idx, 1, box_idxs[:, 0], box_idxs[:, 1]] = 1
            if wall_idxs.shape[0] > 0:
                goals_rep[idx, 2, wall_idxs[:, 0], wall_idxs[:, 1]] = 1

        return goals_rep

    def _get_next_idx(self, curr_idxs: np.ndarray, actions: List[int]) -> np.ndarray:
        actions_np: np.array = np.array(actions)
        next_idxs: np.ndarray = curr_idxs.copy()

        action_idxs = np.where(actions_np == 0)[0]
        next_idxs[action_idxs, 0] = next_idxs[action_idxs, 0] - 1

        action_idxs = np.where(actions_np == 1)[0]
        next_idxs[action_idxs, 0] = next_idxs[action_idxs, 0] + 1

        action_idxs = np.where(actions_np == 2)[0]
        next_idxs[action_idxs, 1] = next_idxs[action_idxs, 1] - 1

        action_idxs = np.where(actions_np == 3)[0]
        next_idxs[action_idxs, 1] = next_idxs[action_idxs, 1] + 1

        next_idxs = np.maximum(next_idxs, 0)
        next_idxs = np.minimum(next_idxs, self.dim - 1)

        return next_idxs

    def __getstate__(self):
        self.states_train = None
        self._surfaces = None

        return self.__dict__


class InteractiveEnv(plt.Axes):
    def __init__(self, env, fig):
        self.env: Sokoban = env

        super(InteractiveEnv, self).__init__(plt.gcf(), [0, 0, 1, 1])

        callbacks = fig.canvas.callbacks.callbacks
        del callbacks['key_press_event']

        self.figure.canvas.mpl_connect('key_press_event', self._key_press)

        self._get_instance()
        self._update_plot()

        self.move = []

    def _get_instance(self):
        states, goals = self.env.get_start_goal_pairs([1000])
        self.state: SokobanState = cast(SokobanState, states[0])
        self.state_goal: Model = self.env.goal_to_model([cast(SokobanGoal, goals[0])])[0]

    def _update_plot(self):
        self.clear()
        rendered_im = self.env.visualize([self.state])[0]
        rendered_im_goal = self.env.visualize([self.state_goal])[0]

        self.imshow(np.concatenate((rendered_im, rendered_im_goal), axis=1))
        self.figure.canvas.draw()

    def _key_press(self, event):
        if event.key.upper() in 'ASDW':
            action: int = -1
            if event.key.upper() == 'W':
                action = 0
            if event.key.upper() == 'S':
                action = 1
            if event.key.upper() == 'A':
                action = 2
            if event.key.upper() == 'D':
                action = 3

            self.state = self.env.next_state([self.state], [action])[0][0]
            self._update_plot()
            if self.env.is_solved([self.state], [self.env.model_to_goal([self.state_goal])[0]])[0]:
                print("SOLVED!")
        elif event.key.upper() in 'R':
            self._get_instance()
            self._update_plot()
        elif event.key.upper() in 'P':
            for i in range(1000):
                self.state = cast(SokobanState, self.env.next_state_rand([self.state])[0][0])
            self._update_plot()


def main():
    env: Sokoban = Sokoban("sokoban")

    fig = plt.figure(figsize=(5, 5))
    interactive_env = InteractiveEnv(env, fig)
    fig.add_axes(interactive_env)

    plt.show()


if __name__ == '__main__':
    main()
