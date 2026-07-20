#
# Copyright (c) 2022 Manufactura de ingenios tecnológicos SL.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#


# This imports the library
from robobopy.Robobo import Robobo

# This creates an instance of the Robobo class with the localhost IP address
rob = Robobo("localhost")

# This connects to the robobo simulator
rob.connect()


# This makes Robobo move straight for 4 seconds
rob.moveWheelsByTime(10, 10, 4)

# This disconnects from the robobo base.
rob.disconnect()
