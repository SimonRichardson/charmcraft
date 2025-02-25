# Copyright 2020-2022 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# For further info, check https://github.com/canonical/charmcraft

"""Infrastructure for common base commands functionality."""

import craft_cli


class BaseCommand(craft_cli.BaseCommand):
    """Subclass this to create a new command.

    The following default attribute is provided beyond craft-cli ones:

    - needs_config: will ensure a config is provided when executing the command

    The subclass must be declared in the corresponding section of main.COMMAND_GROUPS.
    """

    needs_config = False
