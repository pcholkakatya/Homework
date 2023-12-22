import time
class Auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
    def move(self):
        print('Move')
    def birthday(self):
        print(self.age + 1)
    def stop(self):
        print('Stop')


class Truck(Auto):  
    def __init__(self, brand, age, color, mark, weight, max_load):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load
    def move(self):
        print('Attention!')
        super().move()
    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)
        
class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed
    def move(self):
        super().move()
        print('Max speed is', self.max_speed)






