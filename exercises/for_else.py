# Just a demonstration of for-else
from helpers import add_linebreak

# for-else loop
# else block executes when break is NOT encountered

add_linebreak('for-else loop')
lst = range(10)
item = 15

for i in lst:
    if i == item:
        break
else:
	print(f'item having a value of {item} not found in lst')
