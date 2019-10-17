from __future__ import absolute_import, print_function

import tvm
import numpy as np

from tvm import relay
from tvm.relay import testing

# Global declarations of environment.

tgt_host="llvm"
# Change it to respective GPU if gpu is enabled Ex: cuda, opencl, rocm
tgt="cuda"



batch_size = 1
num_class = 1000
image_shape = (3, 224, 224)
data_shape = (batch_size,) + image_shape
out_shape = (batch_size, num_class)

mod, params = relay.testing.resnet.get_workload(
            num_layers=18, batch_size=batch_size, image_shape=image_shape)

# set show_meta_data=True if you want to show meta data
print(mod.astext(show_meta_data=False))



opt_level = 3
target = tvm.target.cuda()
with relay.build_config(opt_level=opt_level):
        graph, lib, params = relay.build_module.build(
                        mod, target, params=params)
