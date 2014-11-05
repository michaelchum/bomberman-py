class Tile(object):

    Empty = 0
    Concrete = 1
    Brick = 2
    Bomb = 3
    Bomberman = 4
    Powerup = 5
    Exit = 6
    Flash = 7

    def __init__(self):
        self.stack = [Tile.Empty]

    def isEmpty(self):
        return self.stack == [Tile.Empty]

    def push(self, tile):
        self.stack.append(tile)

    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)