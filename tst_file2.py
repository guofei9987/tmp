from abc import ABCMeta, abstractmethod
import types
import warnings


class SkoBase(metaclass=ABCMeta):
    def register(self, operator_name, operator, *args, **kwargs):
        '''
        regeister udf to the class
        :param operator_name: string
        :param operator: a function, operator itself
        :param args: arg of operator
        :param kwargs: kwargs of operator
        :return:
        '''

        def operator_wapper(*wrapper_args):
            return operator(*(wrapper_args + args), **kwargs)

        setattr(self, operator_name, types.MethodType(operator_wapper, self))
        return self

    def fit(self, *args, **kwargs):
        warnings.warn('.fit() will be deprecated in the future. use .run() instead.'
                      , DeprecationWarning)
        return self.run(*args, **kwargs)


class Problem(object):
    pass
'''任意一段注释，
genetic algorithm
Parameters
----------------
func : function
    The func you want to do optimal
n_dim : int
    number of variables of func
lb : array_like
    The lower bound of every variables of func
ub : array_like
    The upper bound of every variables of func
constraint_eq : tuple
    equal constraint
constraint_ueq : tuple
    unequal constraint
precision : array_like
    The precision of every variables of func
size_pop : int
    Size of population
max_iter : int
    Max of iter
prob_mut : float between 0 and 1
    Probability of mutation
Attributes
----------------------
Lind : array_like
     The num of genes of every variable of func（segments）
generation_best_X : array_like. Size is max_iter.
    Best X of every generation
generation_best_ranking : array_like. Size if max_iter.
    Best ranking of every generation
Examples
-------------
https://github.com/guofei9987/scikit-opt/blob/master/examples/demo_ga.py

这里插入一段含零宽字符1d
这里插入一段含零宽字符7F
这里插入​一段含零宽字符200B
这里插入‌一段含零宽字符200C
这里插入‍一段含零宽字符200D
这里插入﻿一段含零宽字符FEFF
这里插入⁠一段含零宽字符0x2060
这里插入­一段含零宽字符0x00AD
这里插入一段含零宽字符0x202A

'''
    
