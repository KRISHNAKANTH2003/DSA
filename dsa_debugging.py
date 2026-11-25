class animal:
    def __init__(self,name:str,age:int):
        self._name=str(name)
        self._age=age
    def change_name(self,name):
        self._name=name
    def change_age(self,age):
        self._age=age
    def get_name(self):
        return self._name
    
animal_1=animal("dog",18)
animal_2=animal("cat",4)
animal_3=animal(8,12)
print(animal_3.get_name())