'''
General info
'''


try:
    mydata = [100, 200, 300]
    print(mydata)
    fp1 = open('some_file.txt', 'r')
    a, b = 100, 0
    print(a/b)
except (ZeroDivisionError, FileNotFoundError, IndexError) as er:
    print('error block1', er)
    status = False
except Exception as er:
    print('general error block', er)
    status = False
else:
    print('all is well')
    status = False
# Finally block will be executed even if you put a return statement
# in any of the blocks
finally:
    try:
        fp1.close()
    except Exception: pass