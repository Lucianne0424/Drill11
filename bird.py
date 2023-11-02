import random

from pico2d import load_image

import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
BIRD_SPEED_KMPH = 10.0
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill here
BIRD_TIME_PER_ACTION = 0.5
BIRD_ACTION_PER_TIME = 1.0 / BIRD_TIME_PER_ACTION
BIRD_FRAMES_PER_ACTION = 14

class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x = random.randint(0 + 100, 1600 - 100)
        self.y = 450
        self.dir = 1
        self.frame = 0


    def draw(self):
        # print(self.frame)
        left = int(self.frame) % 5
        bottom = 2 - int(self.frame) // 5
        size_x = 910 // 5
        size_y = 506 // 3
        if self.dir == 1:
            self.image.clip_draw(left * size_x, bottom * size_y, size_x , size_y , self.x, self.y, 50, 50)
        else:
            self.image.clip_composite_draw(left * size_x, bottom * size_y, size_x ,size_y, 0, 'h', self.x, self.y, 50, 50)

    def update(self):
        self.frame = (self.frame + BIRD_FRAMES_PER_ACTION * BIRD_ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * BIRD_SPEED_PPS * game_framework.frame_time
        if self.x > 1600:
            self.dir *= (-1)
        elif self.x < 0:
            self.dir *= (-1)

