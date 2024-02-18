import unittest
import json
from src.room import Room

class TestCustomer(unittest.TestCase):

    FILE_PATH = "data/customer.json"
     
    def test_add_room(self):
        '''
        test if the create room
        '''
        room_1 = Room("1",120)
        room_2 = Room("D01",202.10)
        self.assertEqual(room_1.add_room(), "1")        
        self.assertEqual(room_2.add_room(), "D01")

    def test_invalid_room(self):
        '''
        test if data is valid
        '''
        room_1 = Room("S10",-220)
        room_2 = Room("",220)
        self.assertEqual(room_1.add_room(), None)
        self.assertEqual(room_2.add_room(), None)
        self.assertRaises(TypeError, 'Invalid Input(s), try again')
    
    def test_delete_room(self):
        '''test delete room'''
        room_1 = Room("1",130)
        self.assertEqual(room_1.remove_room("1"), f"room 1 deleted" )
        self.assertEqual(room_1.remove_room("A92"), f"room A92 not found" )

    
    def test_show_room(self):
        '''rest show room'''
        room_1 = Room("D01",130)
        self.assertEqual(room_1.show_room("D01"), f"ID:D01 price:202.1" )
        self.assertEqual(room_1.show_room("A92"), f"room A92 not found")
    
if __name__ == '__main__':
    unittest.main()
