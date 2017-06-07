
# def fib(max):
#     a, b = 0, 1
#     while a < max:
#         yield a
#         a, b = b, a + b
#     # return

class employee:
    
    def __init__(self, name):
        self.__name = name

    def __get_name(self):
        return self.__name


def foo(*var_args):
    if(len(var_args)==1):
        return var_args[0]
    else:
        sum = 0
        for i in range(0, len(var_args)):
            sum +=var_args[i]
        return sum

if __name__ == "__main__":
    print (foo(2, 3, 9))
    emp = employee("Safi")
    print (emp.__get_name())