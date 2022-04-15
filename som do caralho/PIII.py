import random
from winsound import Beep


for i in range(300):

    RandomPith = random.randint(37,3000)
    RandomLeng = random.randint(100, 1000)

    Beep(RandomPith, RandomLeng)