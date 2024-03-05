class test:
    def __init__(self,name,age,hobby): #The __init__()called (as constructor) is called automatically every time the class is being used to create a new object.
        self.name=name
        self.age=age
        self.hobby = hobby
    def display(self):
        print("My name is ",self.name)
        print("My hobby is ",self.hobby)
        print("My age is ",self.age)


#This is a one simple example of how to create a class and create object and call the objects of the class

#Inheritance : When object of the parent class is called by child class
#https://www.geeksforgeeks.org/inheritance-in-python/

class child(test):
    # def __init__(self,name,age,hobby):
    #     # super().__init__(name,age,hobby)
    #     pass
    def child_function(self,name,age,hobby,new_property):
        print('My name is :', name)
        print("My hobby is : ",hobby)
        print("My age is : ",age)
        print("New",new_property)
# obj1= test("Parth",23,"Football")
# obj1.display()    
obj2=child("Zala",69,"Movies")  
obj2.display() 
obj2.child_function("Zala",69,"Movies",'j')    
