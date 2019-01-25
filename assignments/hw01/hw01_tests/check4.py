# begin import modules
from datascience import *
import numpy as np
# end import modules
#begin err msg definition
msg0 = """You need to replace the ... in the solution."""
msg1 = """The value you assign to jobs_q1 should be 1, 2, or 3."""
msg2 = """The value you assign to jobs_q2 should be 1, 2, or 3."""
#end err msg definition
def check4(jobs_q1,jobs_q2):
    if jobs_q1 == ... or jobs_q2 == ...: 
        print(msg0)
    elif not 1 <= jobs_q1 <= 3 :
        print(msg1)
    elif not 1 <= jobs_q2 <= 3 :
        print(msg2)
    else:
        print("Your solution looks ok!")
