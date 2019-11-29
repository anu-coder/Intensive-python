'''
An improved element wise addition implementation of a list
'''


class ImprovedList(list):
    def __init__(self, lst):
        super().__init__(lst)
        
    def __add__(self, other):
        n = len(l1)
        res = [0]*n
        for i in range(n):
            res[i] = self[i] + other[i]
        
        return(res)


if __name__ == "__main__":
    l1 = ImprovedList([1, 2, 3])
    l2 = ImprovedList([4, 5, 6])
    print("l1 = ", l1)
    print("l2 = ", l2)
    print("l1 + l2 = ", l1 + l2)    