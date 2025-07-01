#Type casting
age=20
gpa=3.2
is_student=True
print(type(is_student))
gpa=int(gpa)
print(gpa)
#20 is converted into string from interger even though it's appears same
age=str(age)
print(age)
print(type(age))
#here if you simply type 1 it is integer so it gives Typeerror we should type "1" to make it a string
#we can use age=age+"1" also
age +="1"
print(age)