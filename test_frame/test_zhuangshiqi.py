# def hi(name="yasoob"):
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
#
# a = hi()
# # print(a)  # <function hi.<locals>.greet at 0x000001D0D6D739D8>
# # print(a())  # now you are in the greet() function
# # print(hi()()) # now you are in the greet() function



# def hi():
#     return "hi yasoob!"
#
# # fun=hi
# def doSomethingBeforeHi(func):
#     print("I am doing some boring work before executing hi()")
#     print(func())  # hi yasoob!
#     print(func)  # <function hi at 0x000001C7A4543A60>
#
# doSomethingBeforeHi(hi)


# def a_new_decorator(a_func):
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction  # 装饰器的返回值是一个函数对象
#
# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")
#
# # a_function_requiring_decoration()
#
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)  # 返回函数对象wrapTheFunction
# # now a_function_requiring_decoration is wrapped by wrapTheFunction()
#
# a_function_requiring_decoration()
#
# # func = object
# # I am doing some boring work before executing a_func()
# # I am the function which needs some decoration to remove my foul smell
# # I am doing some boring work after executing a_func()
import logging


def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warning("%s is running" %func.__name__)
        return func(*args)
    return wrapper

@use_logging
def foo():
    print("I am foo")

@use_logging
def bar():
    print("I am bar")

bar()