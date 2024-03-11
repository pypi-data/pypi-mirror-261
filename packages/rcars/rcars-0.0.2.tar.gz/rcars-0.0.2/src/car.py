'''
Created on 10 Mar 2024

@author: robert.valassi
'''
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def getter(self):
        print(f"Car brand: {self.make}\nModel: {self.model}\nModel Year: {self.year}")