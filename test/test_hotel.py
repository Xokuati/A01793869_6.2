import unittest
import json
from src.hotel import Hotel

class TestCustomer(unittest.TestCase):

    FILE_PATH = "data/hotel.json"
     
    def test_add_Hotel(self):
        '''
        test if the create Hotel
        '''
        Hotel_1 = Hotel("Sunset Lodge","London",92839582712)
        Hotel_2 = Hotel("Beachwalk hotel","Paris", 9402929102)
        self.assertEqual(Hotel_1.add_hotel(), "SL2712")        
        self.assertEqual(Hotel_2.add_hotel(), "BP9102")

    def test_invalid_Hotel(self):
        '''
        test if data is valid
        '''
        Hotel_1 = Hotel("Sunset","",-29823.01)
        Hotel_2 = Hotel("","China",222232120)
        self.assertEqual(Hotel_1.add_hotel(), None)
        self.assertEqual(Hotel_2.add_hotel(), None)
        self.assertRaises(TypeError, 'Invalid Input(s), try again')
    
    def test_delete_Hotel(self):
        '''test dekete hotel'''
        Hotel_1 = Hotel("Sunset","China",222232120)
        self.assertEqual(Hotel_1.remove_hotel("SL2712"), f"hotel SL2712 deleted" )
        self.assertEqual(Hotel_1.remove_hotel("SC2120"), f"hotel SC2120 not found" )

    def test_show_Hotel(self):
        '''test show display'''
        Hotel_1 = Hotel("Sunset","China",222232120)
        self.assertEqual(Hotel_1.show_hotel("BP9102"), f"ID:BP9102 name:Beachwalk hotel" )
        self.assertEqual(Hotel_1.show_hotel("SL2712"), f"hotel SL2712 not found")
    
    def test_room_reserve(self):
        Hotel_1 = Hotel("Sunset","China",222232120)
        self.assertEqual(Hotel_1.room_reserve("D01"), f"room D01 is reserved" )
        self.assertEqual(Hotel_1.room_reserve("S92"), f"room S92 not found")  
      
    def test_remove_room_reserve(self):
        Hotel_1 = Hotel("Sunset","China",222232120)
        
        self.assertEqual(Hotel_1.room_reserve("D01"), f"room D01 is reserved" )
        self.assertEqual(Hotel_1.remove_room_reserve("D01"), f"room D01 has removed")
        self.assertEqual(Hotel_1.remove_room_reserve("S92"), f"room S92 not found")
        
if __name__ == '__main__':
    unittest.main()
