'''
Singleton class
'''

import pickle
from functools import wraps

class InstanceExistsError(Exception):
    pass

class InstanceLimitReachedError(Exception):
    pass

# TODO: Create a decorator which can allow creation of an object n times.
def singleton(cls):
    rec = {}

    @wraps(cls)
    def modcls(*args, **kwargs):
        t = pickle.dumps((args, kwargs))
        if not rec.get(t):
            rec[t] = True
            return (cls(*args, **kwargs))
        
        raise InstanceExistsError
    
    return modcls


def limit_instance(n):
    def nrmldeco(cls):
        rec = {}

        @wraps(cls)
        def modcls(*args, **kwargs):
            t = pickle.dumps((args, kwargs))
            try:
                # This comparision will raise TypeError
                # BUG: Not a good idea as TypeError can be
                #      raised in other ways as well.
                # REFACTOR: Use simple if/else instead
                if rec.get(t) < n: 
                    rec[t] += 1
                    o = cls(*args, **kwargs)
                else:
                    raise InstanceLimitReachedError

            except TypeError:
                rec[t] = cls(*args, **kwargs)
                o = cls(*args, **kwargs)

            return(o)

        return(modcls)

    return(nrmldeco)



    
@limit_instance(2)
class LimitedClass:
    pass

@singleton
class SingletonClass:
    pass


if __name__ == "__main__":


    def get_max_instances(cls):
        i = 0
        while(True):
            try:
                o = SingletonClass()
                i += 1
            except InstanceExistsError as e:
                break

        return(i)

    
    for cls in [SingletonClass, LimitedClass]:
        print(f'Could only create {get_max_instances(cls)} instances',
              f'for the class {cls.__name__}')
