for i in range(101):  
    divides_by_3 = (i % 3 == 0)  
    divides_by_5 = (i % 5 == 0)
    if divides_by_3 and divides_by_5:  
        print("FizzBuzz")
    elif divides_by_3 and not divides_by_5:
        print("Fizz")
    elif divides_by_5 and not divides_by_3:
        print("Buzz")
    else:
        print(i)