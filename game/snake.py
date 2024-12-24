from game.constants import BLOCK_SIZE


class Snake:
    def __init__(self, position, direction="RIGHT"):
        self.body = [list(position), [position[0] - BLOCK_SIZE, position[1]],
                     [position[0] - 2 * BLOCK_SIZE, position[1]]]
        self.direction = direction
        self.alive = True

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            new_head = [head[0], head[1] - BLOCK_SIZE]
        elif self.direction == "DOWN":
            new_head = [head[0], head[1] + BLOCK_SIZE]
        elif self.direction == "LEFT":
            new_head = [head[0] - BLOCK_SIZE, head[1]]
        elif self.direction == "RIGHT":
            new_head = [head[0] + BLOCK_SIZE, head[1]]
        self.body.insert(0, new_head)

    def grow(self):
        pass

    def check_collision(self, width, height):
        head = self.body[0]
        if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
            self.alive = False
        for block in self.body[1:]:
            if head == block:
                self.alive = False
