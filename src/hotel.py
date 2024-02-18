'''Módulo que permite adinistrar hoteles'''
import json
from src.room import Room


FILE_PATH = "src/data/hotel.json"


class Hotel:
    '''Contructor del Hotel'''
    def __init__(self, name: str, city: str, number: int):
        self.hotel_id = None
        try:
            self.name = str(name)
            self.city = str(city)
            self.number = int(number)
            self.list_roms = []
            if len(self.name) < 1:
                assert len(self.name) < 1
            elif len(self.city) < 1:
                assert len(self.city) < 1
            elif self.number < 0:
                assert self.number < 0
            else:
                self.hotel_id = "".join([self.name[0], self.city[0],
                                         str(self.number)[-4:]])
        except (NameError, ValueError, AssertionError):
            print('Invalid Input(s), try again')

    def set_name(self, name):
        '''Asigna el nombre al constructor'''
        self.name = name

    def set_city(self, city):
        '''Asigna la ciudad al constructor'''
        self.city = city

    def set_number(self, number):
        '''Asigna el número al constructor'''
        self.number = number

    def get_name(self):
        '''Obiente el nombre al constructor'''
        return self.name

    def get_number(self):
        '''Obiente el número al constructor'''
        return self.number

    def get_city(self):
        '''Obiente la ciudad al constructor'''
        return self.city

    def get_hotel_id(self):
        '''Obtine el id '''
        return self.hotel_id

    def add_hotel(self):
        '''Agrega un nuevo cliente'''
        res = None
        if len(self.name) < 1:
            assert len(self.name) < 1
        elif len(self.city) < 1:
            assert len(self.city) < 1
        elif self.number < 0:
            assert self.number < 0
        else:
            l_hotels = []
            new_hotel = Hotel(name=self.name, city=self.city,
                              number=self.number)
            l_hotels = get_all_hotel()
            l_hotels.append(new_hotel.__dict__)
            with open(FILE_PATH, 'w+', encoding='utf-8') as f:
                json.dump(l_hotels, f)
            res = new_hotel.hotel_id
        return res

    def remove_hotel(self, hotel_id):
        '''Elimina el cliente seleccionado por el id'''
        encontrado = False
        l_hotels = get_all_hotel()
        for n_hotel in l_hotels:
            if n_hotel["hotel_id"] == hotel_id:
                encontrado = True
                l_hotels.remove(n_hotel)
        with open(FILE_PATH, 'w+', encoding='utf-8') as f:
            json.dump(l_hotels, f)
        if encontrado:
            res = f"hotel {hotel_id} deleted"
        else:
            res = f"hotel {hotel_id} not found"
        return res

    def show_hotel(self, id_customer):
        '''Muetra el cliente seleccionado por el id'''
        res = None
        l_hotels = get_all_hotel()
        if len(l_hotels) > 0:
            for n_hotel in l_hotels:
                if n_hotel["hotel_id"] == id_customer:
                    res = f"ID:{n_hotel['hotel_id']} name:{n_hotel['name']}"
        if res is None:
            res = f"hotel {id_customer} not found"
        return res

    def show_hotels(self):
        '''Muetra todos los cliientes'''
        l_hotels = get_all_hotel()
        if len(l_hotels) > 0:
            for n_hotel in l_hotels:
                print(f"ID:{n_hotel['hotel_id']} ame:{n_hotel['name']}" +
                      f"Number:{n_hotel['city']} Mail:{n_hotel['number']}")

    def room_reserve(self, room_id):
        '''reserva un cuarto'''
        encotrado = False
        existe = False
        for room in Room.get_all_rooms(self):
            if room["room_id"] == room_id:
                encotrado = True
                for l_room in self.list_roms:
                    if l_room["room_id"] == room_id:
                        existe = True
                if existe is False:
                    self.list_roms.append(room)
        if encotrado:
            if existe:
                res = f"room {room_id} is reserved"
            else:
                res = f"room {room_id} has reserved"
        else:
            res = f"room {room_id} not found"
        return res

    def remove_room_reserve(self, room_id):
        '''elmina cuarto reservado'''
        encotrado = False
        for room in self.list_roms:
            if room["room_id"] == room_id:
                self.list_roms.remove(room)
                encotrado = True
        if encotrado:
            res = f"room {room_id} has removed"
        else:
            res = f"room {room_id} not found"
        return res


def get_all_hotel():
    '''Obiene todos los hoteles del arhivo json'''
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            res = json.load(f)
            return res
    except FileNotFoundError:
        return []
