#import utils

#numbers = [10, 3, 6, 2]
#maximum = utils.find_max(numbers)
#print(maximum)

#utils.greet_user()
#utils.kg_lbs_converter()

from pathlib import Path

path = Path()
for file in path.glob('*'):
    print(file)


