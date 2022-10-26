from operator import index
from random import randint, random
from tokenize import Number


favorite_number=("98")
for num in favorite_number:
    if favorite_number=="98":
        print('birth year')


import random
random_number=random.randrange(98)
print(random_number)



favorite_number=2
import random
random_number=random.randrange(5)
counter = 0
while favorite_number is not random_number:
    random_number=random.randrange(5)
    counter = counter + 1
    print(random_number)
else:
    # favorite_number+=1
    loops= input (f"it took the computer {counter} tries to get my favorite number")
