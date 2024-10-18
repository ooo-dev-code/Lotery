from Loto import *
import random

# Dictionary of possibles values
result = {
    "value1":None,
    "value2":None,
    "value3":None,
}

# List of the numbers
nums = list(range(1, 4))
random.shuffle(nums)

for i in range(3):
    
    result[f"value{i+1}"]= nums[i-1]
    print(result[f"value{i+1}"])
