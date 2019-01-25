# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg0 = """You need to replace the ... in the solution."""
msg1 = """The value you assign to universities_q2 should be 1, 2, or 3."""
#end err msg definition
def check5_2(universities_q2):
    if universities_q2 == ...: 
        print(msg0)
    elif not 1 <= universities_q2 <= 3 :
        print(msg1)
    else:
        print("Your solution looks ok!")
