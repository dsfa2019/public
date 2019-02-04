# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg1 = """You need to replace the ... in the definition of q1ans
with 1, 2, 3, or 4."""
msg2 = """Your answer should be 1, 2, 3, or 4."""
#end err msg definition
def check1_1(characters_q1):
    if not characters_q1 != ... : 
        print(msg1)
    elif not 1 <= characters_q1 <= 4 : 
        print(msg2)
    else: 
        print("Your solution looks ok!")
