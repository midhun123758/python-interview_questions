print("hello")


def  odd_even(numbers):
    for i in numbers:
        if i%2==0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")



odd_even([1,2,3,4,5,6,7,8,9])