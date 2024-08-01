# def my_func(x):
#     return  2 * x
# L = []
#
# for i in range(5):
#     L.append(my_func(i))
# print(L)

# 列别推导式
# Python 列表推导式（list comprehension）是一种简洁快速创建列表的方法。
# 它的结构是在方括号内，包含一个表达式，后面跟一个 for 子句，然后是零个或多个 for 或 if 子句。
# 返回的列表由表达式计算的结果组成
# K = [my_func(i) for i in range(5)]
# print(K)

#匿名函数与map方法
#匿名函数 lambda  ：通常用于那些简单的、一次性的函数，这样可以避免定义一个完整的函数。

# 错误使用例子，使用还是需要调用
# my_func = lambda x: 2*x
# print(my_func(3))

#正确使用方法
G = [(lambda x:2*x)(i) for i in range(5)]
#对于上述的这种列表推导式的匿名函数映射， Python 中提供了 map 函数来完成，它返回的是一个 map 对象，需要通过 list 转为列表
L= list(map(lambda x: 2*x, range(5)))
print(L)

