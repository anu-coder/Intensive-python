# Given five positive integers, find the minimum and maximum values
# that can be calculated by summing exactly four of the five integers

def miniMaxSum(arr, n, method='A'):

    if method == 'A':
        minval = arr[0]
        maxval = arr[0]
        arr_sum = 0
        i = 0
        while(i < n):
            curval = arr[i]
            arr_sum += curval
            if curval > maxval:
                maxval = curval
            elif curval < minval:
                minval = curval

            i += 1

        min_sum = arr_sum - maxval
        max_sum = arr_sum - minval

    elif method == 'B':
        arr_sum = sum(arr)
        min_sum = arr_sum - max(arr)
        max_sum = arr_sum - min(arr)



    return([min_sum, max_sum])

n = 10**9
arr = list(range(n +1))

print(miniMaxSum(arr, n, method='B'))