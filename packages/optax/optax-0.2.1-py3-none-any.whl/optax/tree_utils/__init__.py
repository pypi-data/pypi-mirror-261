# Copyright 2019 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""The tree_utils sub-package."""

from optax.tree_utils._state_utils import tree_map_params
from optax.tree_utils._tree_math import tree_add
from optax.tree_utils._tree_math import tree_add_scalar_mul
from optax.tree_utils._tree_math import tree_div
from optax.tree_utils._tree_math import tree_l2_norm
from optax.tree_utils._tree_math import tree_mul
from optax.tree_utils._tree_math import tree_ones_like
from optax.tree_utils._tree_math import tree_random_like
from optax.tree_utils._tree_math import tree_scalar_mul
from optax.tree_utils._tree_math import tree_sub
from optax.tree_utils._tree_math import tree_sum
from optax.tree_utils._tree_math import tree_vdot
from optax.tree_utils._tree_math import tree_zeros_like
