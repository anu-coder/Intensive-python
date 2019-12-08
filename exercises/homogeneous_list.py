'''
Function to test if a list is homogeneous 
'''

def is_homo(lst: list, obj_type):
    return(all(map(lambda o: type(o) is obj_type, lst)))


if __name__ == "__main__":
    class Foo:
        pass

    lst = [Foo() for _ in range(10)]
    print(is_homo(lst, Foo))

    class Bar:
        pass

    lst[0] = Bar()
    print(is_homo(lst, Bar)) 