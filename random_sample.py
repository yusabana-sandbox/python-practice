# -*- coding: utf-8 -*-

import random

print(random.randrange(100))

lunch = ['カレー', 'うどん', '寿司']
print(random.choice(lunch))

random.shuffle(lunch)
print(lunch)
