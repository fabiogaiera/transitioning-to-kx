import os

import pykx as kx

print(os.environ.get("QLIC"))
# In case of using .pykx-config file
print(kx.config.pykx_config_locs)

print(kx.q.til(10))
