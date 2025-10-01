# Day 27 :
# Garfical user Interfarence with Tkinter And Function Arguments :

# *argu :
# we can write as many inputs as we want:
def add(*argu):
    print(type(argu))
    sums = sum(argu)
    return sums
print(add(2,4,6))

# **kwargs : key wards arguments
# this make a dictionary of input data

def kaws(**kwargs):
    print(kwargs)
    for key , value in kwargs.items():
        print(key)
        print(value)

kaws(add=3 , multiply=5)