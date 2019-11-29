'''
An implementation of a Polynomial function as a class
'''


class Polynomial:
    def __init__(self, *args):
        self.cnsts = args[::-1]

    def __call__(self, x):
        res = 0
        n = len(self.cnsts)
        for i in range(n):
            p = n-i-1
            res += self.cnsts[p]*(x**p)
            
        return(res)
    
    @classmethod
    def _get_expr(self, p, c):
        '''
        p: power
        c: constant
        
        Returns the formatted expression string,
        '''
        if c == 0:
            return('')
        if p == 0:
            return(str(c))
        
        s = ''
        if c != 1:
            s += str(c)
        
        if p == 1:
            s += f'(x)'
        else:
            s += f'(x^{p})'
        
        return(s)
    
    def __repr__(self):
        s = ''
        n = len(self.cnsts)
        expr_lst = [0]*n
        
        for i in range(n):
            p = n-i-1
            expr_lst[i] = self._get_expr(p, self.cnsts[p])
            
        
        expr = ' + '.join(list(filter(lambda x: x != '', expr_lst)))
        return(expr)


if __name__ == "__main__":
    f = Polynomial(5, 0, 2, 1, 3)
    print(f)
    print('f(0) = ', f(0))