# Just a demonstration of try-except-else-finally
from helpers import add_linebreak

# try-except-else-finally
add_linebreak('try-except-else-finally')
expected_error = NameError
try:
	'a_string' + 1 # TypeError
except expected_error:
	print('exception')
else:
	print('NO exception occured')
finally:
	print('finally, this would run NO MATTER WHAT!')
	print()

# NOTE: If an unexpected_error occurs, finally still runs
#       but no lines after that would run

print('This will not be printed if an unexpected exception occured!')
