# Buyer class.

import os
import time
from Coffee_Operator import CoffeeOperator

class Coffee(CoffeeOperator):
    def __init__(self):
        dict_coffee = CoffeeOperator.get_dict(CoffeeOperator)
        quantity = CoffeeOperator.get_quantity(CoffeeOperator)
        power_status = CoffeeOperator.get_power(CoffeeOperator)

        self.power_status = True       
        print('Welcome User')
        while self.power_status == True:
            self.display(len(self.quantity))
            if self.quantity == [0] or len(self.quantity) == 0:
                print("No Coffee. Turning off")
                self.power_status = False
                break
            else:
                user_input = int(input('Your choice: ')) - 1
                if 0 <= user_input < len(self.quantity):
                    if self.available(user_input) == True:
                        print('Coffee is getting ready, Please pay the cost')
                    self.coffee_cost(user_input)
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Invalid input. There is no coffee at option {}'.format(user_input+1))

    def available(self,user_input):
        if self.quantity[user_input] > 0:
            self.quantity[user_input] -= 1
            return True
        

    def display(self,length):
        for i in [0]:
            try:
                x = self.quantity.index(i)
                self.quantity.pop(x)
                keys_list = list(self.dict_coffee)
                del_x = keys_list[x]
                self.dict_coffee.pop(del_x)
            except ValueError: 
                pass
        for key,value in self.dict_coffee.items():
            print('{} at Rs {}'.format(key,value))
            
    def coffee_cost(self,user_input):
        value = self.dict_coffee.values()
        cost_lst = list(value)
        cost = cost_lst[user_input]       
        jack=True
        while jack:
            cost_input = int(input('Coffee cost: '))
            if cost_input != cost:
                print('Please enter perfect amount of Rs{}'.format(cost))
                jack = True
            else:
                print('Please collect your coffee')
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                jack = False


os.system('cls' if os.name == 'nt' else 'clear')
c = Coffee()