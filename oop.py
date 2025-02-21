"""
creating a class::we use the keyword 'class' i.e.
class MyClass:
"""
class User:
    fullname = "John Muchiri"
    role_id="Student"
    student_id=378743
    is_verified=True
"""
to create a class we use the name of the class followed by a parenthesis() 
i.e.
class =User ()

"""

person = User() #This creates an object for the user class
print(person.role_id) #To access a property use dot notation
"""
1. the __init__() method :is always executed on an object creation
2. the __str__() method :returns string representation
"""


class Student:
    def __init__(self, fullname, role_id, student_id, is_verified):
        self.fullname =fullname
        self.role_id = role_id
        self.student_id = student_id
        self.is_verified = is_verified
    def __str__(self):
        return f"{self.fullname} {self.role_id} {self.student_id} {self.is_verified}"

    #custom class method
    def transform_word (self,msg):
        new_word = self.fullname.upper()
        role = self.role_id.upper()
        print(msg)
        result =f"{new_word} ,{role},"
        return result


        #$ create an object
s1= Student("John Muchiri","Student",3748684,True)
s2= Student("Hidah Njambi","Student",3894,False)
s3= Student("Joseph M","lecturer",768,True)
print(s1)
print(s2)
print(s3)
print(s1.fullname)
# How to print  object methods
print(s2.transform_word("TRANSFORM SUCCESS"))
print(s3.transform_word("TRANSFORM SUCCESS"))
#How to modify object properties
s1.fullname = "John "
print(s1)
s2.role_id="Staff"
print(s2)
#adding a new property to the object
s2.nationality="Canada"
print(s2)
#how to delete object properties
del s2.fullname
print(s1)
#delete object  properties : use del keyword
del s2
print(s2)