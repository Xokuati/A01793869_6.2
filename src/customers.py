'''Módulo que permite crear modificar y eliminar clientes'''
import json

FILE_PATH = "src/data/customer.json"


class Customer:
    '''Contructor del cliente'''
    def __init__(self, name: str, lname: str, number: int):
        self.customer_id = None
        try:
            self.name = str(name)
            self.lname = str(lname)
            self.number = int(number)
            if self.number < 0:
                assert self.number < 0
            elif len(self.lname) < 1:
                assert len(self.lname) < 1
            else:
                self.customer_id = "".join([self.name[0], self.lname[0],
                                            str(self.number)[-4:]])
        except (NameError, ValueError, AssertionError):
            print('Invalid Input(s), try again')

    def set_name(self, name):
        '''Asigna el nombre al constructor'''
        self.name = name

    def set_number(self, number):
        '''Asigna el número al constructor'''
        self.number = number

    def get_lname(self):
        '''Obiente el lnombre al constructor'''
        return self.lname

    def get_number(self):
        '''Obiente el número al constructor'''
        return self.number

    def get_customer_id(self):
        '''Obtine el id '''
        return self.customer_id

    def add_customer(self):
        '''Agrega un nuevo cliente'''
        res = None
        if self.number < 0:
            assert self.number < 0
        elif len(self.lname) < 1:
            assert len(self.lname) < 1
        else:
            customers = []
            new_customer = Customer(name=self.name,
                                    lname=self.lname, number=self.number)
            customers = get_all_customer()
            customers.append(new_customer.__dict__)
            with open(FILE_PATH, 'w+', encoding='utf-8') as f:
                json.dump(customers, f)
            res = new_customer.customer_id
        return res

    def remove_customer(self, customer_id):
        '''Elimina el cliente seleccionado por el id'''
        encontrado = False
        customers = get_all_customer()
        for n_customer in customers:
            if n_customer["customer_id"] == customer_id:
                customers.remove(n_customer)
                encontrado = True
        with open(FILE_PATH, 'w+', encoding='utf-8') as f:
            json.dump(customers, f)
        if encontrado:
            res = f"Customer {customer_id} deleted"
        else:
            res = f"Customer {customer_id} not found"
        return res

    def show_customer(self, id_customer):
        '''Muetra el cliente seleccionado por el id'''
        res = None
        customers = get_all_customer()
        if len(customers) > 0:
            for cust in customers:
                if cust["customer_id"] == id_customer:
                    res = f"ID:{cust['customer_id']} Name:{cust['name']}"
        if res is None:
            res = f"Customer {id_customer} not found"
        return res

    def show_customers(self):
        '''Muetra todos los cliientes'''
        customers = get_all_customer()
        if len(customers) > 0:
            for customer in customers:
                print(f"ID:{customer['id_customer']} Name:{customer['name']}" +
                      f"Number:{customer['number']} Mail:{customer['email']}")


def get_all_customer():
    '''Obiene todos los clietes del arhivo json'''
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            res = json.load(f)
            return res
    except FileNotFoundError:
        return []
