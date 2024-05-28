class JustException(Exception):
    pass


x = 2

try:
    raise JustException(" Error from custom Class ")
    # print(x/1)
    # if not type(x) is str:
    #     raise TypeError("This is not string")
except NameError:
    print("That is an error: Name Error")
except ZeroDivisionError:
    print("That is an error: Zero Division Error")
except Exception as error:
    print(error)
else:
    print("No Errors")
finally:
    print("This is Finally block")
