# functions are variables in python. They can be passed around.

# Example

def greet(test_func):
    test_func()


def greeting():
    print("Hello there")


#greet(greeting)


#Higher Order Function (HOC)
# Either accepts a function or returns a function

#Decorator = wrapper function, allows added functionality


def wrapper_func(func):
    stars = '*' * 10
    def wrap_func():
        print(stars)
        func()
        print(stars)
    return wrap_func

@wrapper_func
def hello():
    print("Hello There")


hello()
