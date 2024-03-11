from typing import Any, List, Optional
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.parameter import Parameter
from torch import Tensor
import numpy as np


class SPLASH(nn.Module):
    def __init__(self, num_hinges: int = 5, init: str = "RELU"):
        super().__init__()
        assert num_hinges > 0, "Number of hinges should be greater than zero, but is %s" % num_hinges
        assert ((num_hinges + 1) % 2) == 0, "Number of hinges should be odd, but is %s" % num_hinges
        init = init.upper()

        self.num_hinges: int = num_hinges
        self.num_each_side: int = int((self.num_hinges + 1) / 2)

        self.hinges: List[float] = list(np.linspace(0, 2.5, self.num_each_side))

        self.output_bias: Parameter = Parameter(torch.zeros(1), requires_grad=True)

        if init == "RELU":
            self.coeffs_right: Parameter = Parameter(torch.cat((torch.ones(1), torch.zeros(self.num_each_side - 1))),
                                                     requires_grad=True)
            self.coeffs_left: Parameter = Parameter(torch.zeros(self.num_each_side), requires_grad=True)
        elif init == "LINEAR":
            self.coeffs_right: Parameter = Parameter(torch.cat((torch.ones(1), torch.zeros(self.num_each_side - 1))),
                                                     requires_grad=True)
            self.coeffs_left: Parameter = Parameter(torch.cat((-torch.ones(1), torch.zeros(self.num_each_side - 1))),
                                                    requires_grad=True)
        else:
            raise ValueError("Unknown init %s" % init)

    def forward(self, x):
        output: Tensor = torch.zeros_like(x)

        # output for x > 0
        for idx in range(self.num_each_side):
            output = output + self.coeffs_right[idx] * torch.clamp(x - self.hinges[idx], min=0)

        # output for x < 0
        for idx in range(self.num_each_side):
            output = output + self.coeffs_left[idx] * torch.clamp(-x - self.hinges[idx], min=0)

        output = output + self.output_bias

        return output


class LinearAct(nn.Module):
    def __init__(self):
        super().__init__()
        self.dummy = 1

    def forward(self, x):
        self.dummy = 1  # so PyCharm does not complain
        return x


def get_act_fn(act: str):
    act = act.upper()
    if act == "RELU":
        act_fn = nn.ReLU()
    elif act == "ELU":
        act_fn = nn.ELU()
    elif act == "SIGMOID":
        act_fn = nn.Sigmoid()
    elif act == "TANH":
        act_fn = nn.Tanh()
    elif act == "SPLASH":
        act_fn = SPLASH()
    elif act == "LINEAR":
        act_fn = LinearAct()
    else:
        raise ValueError("Un-defined activation type %s" % act)

    return act_fn


class ResnetModel(nn.Module):
    def __init__(self, resnet_dim: int, num_resnet_blocks: int, out_dim: int, batch_norm: bool,
                 weight_norm: bool = False, layer_act: str = "RELU"):
        super().__init__()
        self.blocks = nn.ModuleList()
        self.act_fns = nn.ModuleList()

        # resnet blocks
        for block_num in range(num_resnet_blocks):
            block_net = FullyConnectedModel(resnet_dim, [resnet_dim] * 2, [batch_norm] * 2, [layer_act, "LINEAR"],
                                            weight_norms=[weight_norm] * 2)
            module_list: nn.ModuleList = nn.ModuleList([block_net])

            self.blocks.append(module_list)
            self.act_fns.append(get_act_fn(layer_act))

        # output
        self.fc_out = nn.Linear(resnet_dim, out_dim)

    def forward(self, x):
        # resnet blocks
        module_list: nn.ModuleList
        for module_list in self.blocks:
            res_inp = x
            for module in module_list:
                x = module(x)

            x = F.relu(x + res_inp)

        # output
        x = self.fc_out(x)
        return x


class FullyConnectedModel(nn.Module):
    def _forward_unimplemented(self, *input_val: Any) -> None:
        pass

    def __init__(self, input_dim: int, layer_dims: List[int], layer_batch_norms: List[bool], layer_acts: List[str],
                 weight_norms: Optional[List[bool]] = None):
        super().__init__()
        if weight_norms is None:
            weight_norms = [False] * len(layer_dims)
        self.layers: nn.ModuleList[nn.ModuleList] = nn.ModuleList()

        # layers
        for layer_dim, batch_norm, act, weight_norm in zip(layer_dims, layer_batch_norms, layer_acts, weight_norms):
            module_list = nn.ModuleList()

            # linear
            if weight_norm:
                module_list.append(nn.utils.weight_norm(nn.Linear(input_dim, layer_dim)))
            else:
                module_list.append(nn.Linear(input_dim, layer_dim))

            # batch norm
            if batch_norm:
                module_list.append(nn.BatchNorm1d(layer_dim))

            # activation
            module_list.append(get_act_fn(act))
            self.layers.append(module_list)

            input_dim = layer_dim

    def forward(self, x):
        x = x.float()

        module_list: nn.ModuleList
        for module_list in self.layers:
            for module in module_list:
                x = module(x)

        return x


class Conv2dModel(nn.Module):
    def _forward_unimplemented(self, *input_val: Any) -> None:
        pass

    def __init__(self, chan_in: int, channel_sizes: List[int], kernel_sizes: List[int], paddings: List[int],
                 layer_batch_norms: List[bool], layer_acts: List[str], strides: Optional[List[int]] = None,
                 transpose: bool = False, weight_norms: Optional[List[bool]] = None,
                 dropouts: Optional[List[float]] = None):
        super().__init__()
        self.layers: nn.ModuleList[nn.ModuleList] = nn.ModuleList()
        if strides is None:
            strides = [1] * len(channel_sizes)

        if weight_norms is None:
            weight_norms = [False] * len(channel_sizes)

        if dropouts is None:
            dropouts = [0.0] * len(channel_sizes)

        # layers
        for chan_out, kernel_size, padding, batch_norm, act, stride, weight_norm, dropout in \
                zip(channel_sizes, kernel_sizes, paddings, layer_batch_norms, layer_acts, strides, weight_norms,
                    dropouts):

            module_list = nn.ModuleList()

            # linear
            if transpose:
                conv_layer = nn.ConvTranspose2d(chan_in, chan_out, kernel_size, padding=padding, stride=stride)
            else:
                conv_layer = nn.Conv2d(chan_in, chan_out, kernel_size, padding=padding, stride=stride)

            if weight_norm:
                conv_layer = nn.utils.weight_norm(conv_layer)

            module_list.append(conv_layer)

            # batch norm
            if batch_norm:
                module_list.append(nn.BatchNorm2d(chan_out))

            # activation
            module_list.append(get_act_fn(act))

            # dropout
            if dropout > 0.0:
                module_list.append(nn.Dropout(dropout))

            self.layers.append(module_list)

            chan_in = chan_out

    def forward(self, x):
        x = x.float()

        module_list: nn.ModuleList
        for module_list in self.layers:
            for module in module_list:
                x = module(x)

        return x


class ResnetConv2dModel(nn.Module):
    def _forward_unimplemented(self, *input_val: Any) -> None:
        pass

    def __init__(self, resnet_channels: int, kernel_size: int, padding: int, num_resnet_blocks: int, batch_norm: bool,
                 act: str):
        super().__init__()
        self.blocks = nn.ModuleList()
        self.block_act_fns = nn.ModuleList()

        # resnet blocks
        for block_num in range(num_resnet_blocks):
            block_net = Conv2dModel(resnet_channels, [resnet_channels] * 2, [kernel_size] * 2, [padding] * 2,
                                    [batch_norm] * 2, [act, "LINEAR"])
            module_list: nn.ModuleList = nn.ModuleList([block_net])

            self.blocks.append(module_list)
            self.block_act_fns.append(get_act_fn(act))

    def forward(self, x):
        # resnet blocks
        module_list: nn.ModuleList
        for module_list, act_fn in zip(self.blocks, self.block_act_fns):
            res_inp = x
            for module in module_list:
                x = module(x)

            x = act_fn(x + res_inp)

        return x
