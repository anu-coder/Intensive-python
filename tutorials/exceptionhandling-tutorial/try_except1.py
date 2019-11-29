'''
General info
'''


# Since this will be interpreted line-by-line
# the general exception block will be executed
# So the general exception should be at the end
try:
    open('nsjnd', 'r')
except Exception:
    print('general error block')
except FileNotFoundError:
    print('filenotfounderror block')