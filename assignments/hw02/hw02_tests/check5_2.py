# begin import modules
from datascience import *
import numpy as np
from numbers import Number
# end import modules
#begin err msg definition
msg1 = """Your answer should be 1, 2, or 3."""
#end err msg definition
def check5_2(cumulative_sum_answer):
	if not isinstance(cumulative_sum_answer, Number):
		print(msg1)
	elif not 1 <= cumulative_sum_answer <= 3: 
		print(msg1)
	else:
		print("Your answer is in the correct form.")
