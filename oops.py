#class Car:
#    def __init__(self,brand,model):  #__init__ is a constructor it will just get call the momement the class is called
#       self.brnd=brand
#       self.modl=model

# if __name__=="__main__":  
#     my_car= Car("honda",'1X23X5')
#     print(my_car.brnd,my_car.modl)


#     my_car2=Car("TATA","GH45x")
#     print(my_car2.brnd)


class Car:
    def __init__(self,brand,model):
        self.br=brand
        self.md=model
    def getname(self):
        return "hello world"
class ElectricCar(Car):
    def __init__(self,brand,model,capacity):
        super().__init__(brand,model)
        self.cap=capacity

tesla=ElectricCar('hello','hhh','90kwh')

print(tesla.br,tesla.cap)
print(tesla.getname())
