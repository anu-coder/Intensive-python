# Define a function that takes a list of lists and returns a new list of
# lists with a student's name and their average grade in each sublist.

from .conv_to_num import conv_to_num
from statistics import mean

def average_grade(lst):
    """ Return students' names and their average grades.

    >>> average_grade([['Bob', 56, 80, 72, 90], ['Alice', 60, 88, 44, 70]])
    [['Bob', 74.5], ['Alice', 65.5]]
    """
    res = []
    for stdnt in lst:
        name, avg = stdnt[0], mean(conv_to_num(stdnt[1:]))
        res.append([name, avg])


    return(res)


def main():
    print(average_grade([['Bob', '56', '80', '72', '90'],
                         ['Alice', 60, 88, 44, 70]]))



if __name__ == '__main__':
    main()
