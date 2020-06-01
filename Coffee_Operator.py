from Machine import Machine
class CoffeeOperator(Machine):
    
    def __init__(self):
        Machine.dict_coffee
        Machine.quantity
        if Machine.power_status == False:
            self.power_on()
        while Machine.power_status == True:
            print('=====================================')
            print('Welcome Operator')
            choice = int(input('1. Add new coffee\n2. Modify Price\n3. Modify Quantity\n4. Power On for the user\n5. Power Off\n'))
            if choice == 1:
                self.add_coffee()
            elif choice == 2:
                self.modify_price()
            elif choice == 3:
                self.modify_quantity()
            elif choice == 4:
                self.power_on()
                from Coffee_Buyer import Coffee
                Machine.power_status = False
            elif choice == 5:
                self.power_off()
            else:
                print('Invalid Input') 

    def power_on(self):
        Machine.power_status = True

    def power_off(self):
        Machine.power_status = False
        return Machine.power_status

    def print_values(self):
        print('=====================================')
        print('List of Coffee: ')
        print('Coffee | Cost | Quantity')

        key_lst = list(Machine.dict_coffee)

        value = Machine.dict_coffee.values()
        value_lst = list(value)

        for i in range(len(key_lst)):
            print('{} | {} | {} '.format(key_lst[i],value_lst[i],Machine.quantity[i]))


    def add_coffee(self):
        name= input('New coffee name: ')
        price = int(input('New coffee price: '))
        quantity = int(input('New coffee Quality: '))
        Machine.dict_coffee.update({name:price})
        Machine.quantity.append(quantity)
        self.print_values()
        
    def modify_price(self):
        name = input('Enter name of coffee: ')
        if name in Machine.dict_coffee:
            update_price = int(input('Updated price: '))
            Machine.dict_coffee[name] = update_price
            print('Cost of {} is Rs{}'.format(name,update_price))
        else:
            print('Invalid coffee name')
         
    def modify_quantity(self):
        print('Available quantity:')
        key_lst = list(Machine.dict_coffee)
        for i in range(len(key_lst)):
            print('Quantity of {} is {}'.format(key_lst[i],Machine.quantity[i]))
        name = input('Enter name of coffee: ')
        if name in Machine.dict_coffee:
            add_remove = int(input('1.Add more\n2.Remove existing\n'))
            change_quantity = int(input('Update quantity: '))
            name_lst = list(Machine.dict_coffee)
            index_name = name_lst.index(name)
            if add_remove == 1:
                Machine.quantity[index_name] += change_quantity
                self.print_values()
            elif add_remove == 2:
                if Machine.quantity[index_name] >= change_quantity:
                    Machine.quantity[index_name] -= change_quantity
                    self.print_values()
                else:
                    print('You have exceed the quantity')
        
    

    def get_dict(self):
        return Machine.dict_coffee
    def get_quantity(self):
        return Machine.quantity
    def get_power(self):
        return Machine.power_status

if __name__ == "__main__":
    opr = CoffeeOperator()
