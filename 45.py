class invalid age exception(exception):
    "raised when the input value is less than 18"
    pass
number=18
by:
    input_num=int(input("enter a number:"))
    if input_num<number:
        raise invalid age exception
    else:
        print("eligible to vote")
        except.invalid age exception:
            print("exception occured:invalid age")
