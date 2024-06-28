import os
import json
import inquirer

#HER BIR CLASS ICIN AYRI PYTHON DOSYASI OLUSTUR!!!!


#class Common:
#dosyaya yazma ve dosyayi okuma fonksyionlari static olarak burada bulunacak

#class School:
#employee, student ve teacher listeleri burada tutulacak

class Employee:
    #NAME, SURNAME AGE, GENDER VARIABLELARINNIN ISLEMLERI BURADA OLACAK
    def name(self):
        raise NotImplementedError
    def surname(self):
        raise NotImplementedError
    def age(self):
        raise NotImplementedError
    def gender(self):
        raise NotImplementedError
    
class Student(Employee):
    #set, get
    def __init__(self, name=None, surname=None, age=None, gender=None, classes=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.classes = classes
        
    def input_name(self):
        self.name = input("What is your name? ")
        
    def input_surname(self):
        self.surname = input("What is your surname? ")
        
    def input_age(self):
        self.age = input("What is your age? ")
        
    def input_gender(self):
        self.gender = input("What is your gender? ")
        
    def input_classes(self):
        self.classes = input("Which class do you go? ")

student = Student()
student.input_name()
student.input_surname()
student.input_age()
student.input_gender()
student.input_classes()

print("Student information:")
print(f"Name: {student.name}")
print(f"Surname: {student.surname}")
print(f"Age: {student.age}")
print(f"Gender: {student.gender}")
print(f"Class: {student.classes}")