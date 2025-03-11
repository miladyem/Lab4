from enum import Enum


class Symbol(Enum):
    """
    Symbols that may appear in the level file
    """

    BOX = "$"
    BOX_ON_GOAL = "*"
    PLAYER = "@"
    PLAYER_ON_GOAL = "+"
    GOAL = "."
    WALL = "#"
    FLOOR = "-"


class MoveResponse(Enum):
    INVALID_WALL = "can't push walls"
    INVALID_BOX = "can't push this box"
    VALID = "valid"


class SokobanModel:
    def __init__(self, level_data):
        """ level_data is a list of strings"""

        self.walls = set()
        self.boxes = set()
        self.goals = set()

        # We'll assume the level data is well formed (all lines are the
        # same length).
        self.size = [len(level_data[0].strip()), len(level_data)]

        for y, row in enumerate(level_data):
            for x, symbol in enumerate(row.strip()):
                pos = (x, y)
                match symbol:
                    case Symbol.BOX.value:
                        self.boxes.add(pos)
                    case Symbol.BOX_ON_GOAL.value:
                        self.boxes.add(pos)
                        self.goals.add(pos)
                    case Symbol.PLAYER.value:
                        self.player = pos
                    case Symbol.PLAYER_ON_GOAL.value:
                        self.player = pos
                        self.goals.add(pos)
                    case Symbol.GOAL.value:
                        self.goals.add(pos)
                    case Symbol.WALL.value:
                        self.walls.add(pos)
                    # Anything that's not a goal/player/box/wall is implied to
                    # be a floor. We don't keep track of floors.

    def is_empty(self, x, y):
        pos = (x, y)
        # `return pos not in self.walls.union(self.boxes)` would be equivalent
        # the following code is however easier to read
        if pos in self.walls:
            return False
        if pos in self.boxes:
            return False
        return True

    def move(self, dx, dy):
        (x, y) = self.player
        (nx, ny) = (x + dx, y + dy)  # nx, ny are where the player is trying to go
        if self.is_empty(nx, ny):
            self.player = (nx, ny)
            return MoveResponse.VALID
        elif (nx, ny) in self.boxes:
            # nnx, nny are where the box is trying to go
            (nnx, nny) = (nx+dx, ny+dy)
            if self.is_empty(nnx, nny):
                self.boxes.remove((nx, ny))
                self.boxes.add((nnx, nny))
                self.player = (nx, ny)
                return MoveResponse.VALID
            else:
                return MoveResponse.INVALID_BOX
        else:
            return MoveResponse.INVALID_WALL

    def width(self):
        return self.size[0]

    def height(self):
        return self.size[1]

    def symbol(self, x, y):
        pos = (x, y)
        if pos in self.goals:
            if pos in self.boxes:
                return Symbol.BOX_ON_GOAL
            if pos == self.player:
                return Symbol.PLAYER_ON_GOAL
            return Symbol.GOAL
        if pos in self.boxes:
            return Symbol.BOX
        if pos == self.player:
            return Symbol.PLAYER
        if pos in self.walls:
            return Symbol.WALL
        return Symbol.FLOOR
    
    def is_level_completed(self):
        # Checks if all goals are covered by boxes.
        # A level is completed when all the goal positions (".") are covered by boxes ("*").
        for pos in self.goals:
            if pos not in self.boxes:
                return False
        return True

    def check_level_status(self):
        """Check if the level is completed and print 'success'."""
        if self.is_level_completed():
            print("success")
            return True
        return False