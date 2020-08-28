# Bubble sort algorithm

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr) # loop to get the length

    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                swap(j, j+1)




def main():
    arr = [64, 34, 99, 12, 22, 11, 90]
    print(arr)
    bubble_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()