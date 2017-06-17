number  = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

a = 1
b = 2

print("bigger") if a > b else print("smaller")

student_names = ["Mark", "Katrina", "Jessica"]

for name in student_names:
    print("Student name is {0}".format(name))

x=0
for index in range(10):
    x+=10
    print("The value of X is {0}".format(x))
x=0
for index in range(5,10):
    x+=10
    print("The value of X is {0}".format(x))

x=0
for index in range(5,10,2):
    x+=10
    print("The value of X is {0}".format(x))