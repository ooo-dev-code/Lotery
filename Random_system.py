from Loto import *
import random

result = {
    "value1":None,
    "value2":None,
    "value3":None,
}
   
nums = list(range(1, 4))
random.shuffle(nums)

for i in range(3):
    
    result[f"value{i+1}"]= nums[i-1]
    print(result[f"value{i+1}"])
