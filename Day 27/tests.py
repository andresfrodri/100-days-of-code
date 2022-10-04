def add(*args):
    return sum(args)

print(add(1,2,4,56,3,5,3,424,5,0,3,3,2,2))

def calculate(n,**kwargs):
    n += kwargs['add']
    print(f'{n-kwargs["add"]} plus {kwargs["add"]} is {n}')
    n *= kwargs['multiply']    
    print(f'{n//kwargs["multiply"]} times {kwargs["multiply"]} is {n}')
    

calculate(2,add=1, multiply=4)    


class Car():
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.wheels = kw.get('wheels')
        self.doors = kw.get('doors')
        
my_car = Car(make='Honda', doors=3)
print(my_car.doors)