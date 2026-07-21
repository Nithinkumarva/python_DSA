'''#access modifiers
class A:
    def __init__(self,name,age,gender):
        self.__name=name #private variable can be accessed of same class whitch defined with
        self._age=age#protected variable can be accessed within same class  withch defined with 
        self.gender=gender#public variable can be accessed anywhere witch defined without any accesss modifier witch defined with no prefix
    def display(self):
        print(self.__name)
        print(self._age)
        print(self.gender)
    def setage(self,age):
        self._age=age
    def getage(self):
        return self._age
a1=A("Nithin",22,"male")
a2=A("divya",20,"female")
print(a1.display())
a1.setage(23)
print(a1.display())'''

'''from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def get_balance(self):
        return self.__balance
    @abstractmethod
    def calculate_interest(self):
        pass
class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.get_balance()*0.05'''
    
'''#inheritance
class Animal:
    def __init__(self):
        print("Animal class")
    class dog(Animal):
        def sound(self):
            print("woof")
    class cat(Animal):
        def sound(self):
            print("meow")'''
    