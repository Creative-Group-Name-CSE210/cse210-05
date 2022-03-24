from itertools import cycle
import constants
from game.scripting.action import Action
from game.casting.actor import Actor
from game.shared.color import Color

class GrowTailAction(Action):

    def execute(self, cast, script):

        cycle1 = cast.get_first_actor('snakes')
        cycle2 = cast.get_second_actor('snakes')

        head = cycle1.get_head()
        if head.get_color() == Color(255,255,255):
            pass
        elif head.get_color() == Color(0,255,0):
            cycle1.grow_tail(1)
            cycle2.grow_tail(1)

