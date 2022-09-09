#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2022/9/6 13:36
# @Author: xzxiao

class Car:
    wheels = 4
    energy = "gasoline"
    
    def __init__(self, manufacturer, model, plate_number, 
                 capacity=5, produced_date="20220906"):
        self.manufacturer = manufacturer
        self.model = model
        self.plate_number = plate_number
        self.capacity = capacity
        self.produced_date = produced_date
        self.__speed = 0
        self.__odometer = 0
        
    def speedup(self, n):
        self.__speed += n
        
    def slowdown(self, n):
        self.__speed -= n

    def get_description(self):
        print("生产商:", self.manufacturer)
        print("车型:", self.model)
        print("车牌号:", self.plate_number)
        print("生产日期:", self.produced_date)
        print("载客量:", self.capacity)
        
    def change_odometer(self, mileage):
        self.__odometer = mileage
        
    def increment_odometer(self, mileage):
        self.__odometer += mileage

    def read_odometer(self):
        print("行驶里程:", self.__odometer)

    def speed(self):
        print("当前速度:", self.__speed)


class ElectricCar(Car):
    energy = "Electricity"
    
    def __init__(self, manufacturer, model, plate_number,
                 battery_capacity, battery_type, distance,
                 capacity=5, produced_date="20220906", ):
        super().__init__(manufacturer, model, plate_number,
                         capacity, produced_date)
        self.battery_capacity = battery_capacity
        self.battery_type = battery_type
        self.distance = distance

    def charge(self):
        self.distance += 500

    def get_description(self):
        super().get_description()
        print("电池容量:", self.battery_capacity)
        print("电池类型:", self.battery_type)
        print("续航里程:", self.distance)


my_car = Car("Audi", "A4", "京A66666")
my_car.get_description()
my_car.speed()
my_car.speedup(100)
my_car.speed()
my_car.slowdown(40)
my_car.speed()
my_car.increment_odometer(100)
print("\n")
my_car.get_description()

print("\n")
new_car = ElectricCar("Tesla", "Model S", "京A666666",
                      "500 km", "Tesla Super Battery", 500)
new_car.get_description()
print("\n")
new_car.charge()
new_car.get_description()
new_car.speedup(120)
new_car.slowdown(100)
new_car.speed()
new_car.increment_odometer(75)
new_car.read_odometer()
