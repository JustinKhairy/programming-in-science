# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def get_day_name(day_number):
    if day_number==1:
        result=("it is a monday")
    elif day_number==2:
        result=("it is a tuesday")
    elif day_number==3:
        result=("it is a wednesday")
    elif day_number==4:
        result=("it is a thursday")
    elif day_number==5:
        result=("it is a friday")
    elif day_number==6:
        result=("it is a saturday")
    elif day_number==7:
        result=("it is a sunday")
    else:
        result=("this is not a proper day number")
    return result

day_number=float(input("what number of the week is it?"))    
print(get_day_name(day_number))


# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def check_weekday_or_weekend(day_number):
    if day_number <=5 and day_number>=1:
        result=("it is a weekday")
    elif day_number >=8 or day_number<=0:
        result=("this is not a proper day number")
    else:
        result=("it is a weekend")
    return result

print(check_weekday_or_weekend(day_number))