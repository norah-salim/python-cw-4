def my_name(name):
    print("My name is "+ name )
my_name("norah")


def my_meal(food,drink):
    print("I like to eat " + food + " and while drinking  " + drink)
my_meal("Hamburger","Cola")


def cube(number):
    return number*number*number
result = cube(3)
print(result)

def by_three(number):
    if number %  3==0:
        return cube(number)
    else:
        return False
number2 = 4
result2 = by_three(number2)
print(result2)