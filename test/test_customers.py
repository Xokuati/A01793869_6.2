import unittest
import json
from src.customers import Customer

class TestCustomer(unittest.TestCase):

    FILE_PATH = "data/customer.json"
  
    # def setUp(self):
    #     customer_1 = Customer('Miguie','Diaz',6354721598)
    #     customer_1.add_customer()
    
    def test_add_customer(self):
        '''
        test if the create a reservation
        '''
        customer_1 = Customer('Luis','Hernandez',2354259874)
        customer_2 = Customer('David','N',9023812923.00)
        self.assertEqual(customer_1.add_customer(), "LH9874")        
        self.assertEqual(customer_2.add_customer(), "DN2923")

    def test_invalid_customer(self):
        '''
        test if data is valid
        '''
        customer_1 = Customer('Ana','M',-2354259874)
        self.assertEqual(customer_1.add_customer(), None)
        self.assertRaises(TypeError, 'Invalid Input(s), try again')

        customer_2 = Customer('Karen','',23542598.02)
        self.assertEqual(customer_2.add_customer(), None)
        self.assertRaises(TypeError, 'Invalid Input(s), try again')

    
    def test_delete_customer(self):
        ''''''
        customer_1 = Customer('Miguie','Diaz',6354721598)
        self.assertEqual(customer_1.remove_customer("LH9874"), f"Customer LH9874 deleted" )
        self.assertEqual(customer_1.remove_customer("AM9874"), f"Customer AM9874 not found" )

    
    def test_show_customer(self):
        '''Muestra el cliente'''
        customer_1 =  Customer('David','N',9023812923.00)
        self.assertEqual(customer_1.show_customer("DN2923"), f"ID:DN2923 Name:David" )
        self.assertEqual(customer_1.show_customer("LQ9874"), f"Customer LQ9874 not found")

if __name__ == '__main__':
    unittest.main()
