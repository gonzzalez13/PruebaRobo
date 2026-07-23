
from behaviour_mod.behaviour import Behaviour


class SearchColor(Behaviour):
    def __init__(self, robot, supress_list, params, color):
        super().__init__(robot, supress_list, params)
        self.color = color
