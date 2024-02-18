a = int(input("Enter the numerator:"))
b = int(input("Enter the denominator: "))

class EqualError(Exception):
    pass
class NegativeError(Exception):
    pass
def div_no(x,y):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    elif(b==a):
        raise EqualError("WE dont need equal numbers for division")
    elif(b<0):
        raise NegativeError("Please make sure you enter a positive number")
    else:
        return a/b
try:
    result = div_no(a,b)
    print(result)
except ZeroDivisionError as error:
    print("Error occured: ",str(error))

except NegativeError as error:
    print("Error Occured: ",str(error))
except EqualError as error:
    print("Error Occured: ", str(error))