
'''Módulo que permite administrar los cuartos'''
import json
FILE_PATH = "src/data/room.json"


class Room():
    '''Contructor de la clase cuartos'''
    def __init__(self, room_id: str, price: int):
        try:
            self.price = float(price)
            self.room_id = str(room_id)
            self.boked = False
            if self.price < 0:
                assert self.price < 0
            elif len(self.room_id) < 1:
                assert len(self.room_id) < 1
        except (NameError, ValueError, AssertionError):
            print('Invalid Input(s), try again')

    def get_room_price(self):
        '''obtiene precio del cuarto'''
        return self.price

    def get_room_booked(self):
        '''valida si el cuarto esta activo'''
        return self.boked

    def add_room(self):
        '''Agrega un nuevo cliente'''
        res = None
        if self.price < 0:
            assert self.price < 0
        elif len(self.room_id) < 1:
            assert len(self.room_id) < 1
        else:
            rooms = []
            new_room = Room(room_id=self.room_id, price=self.price)
            rooms = self.get_all_rooms()
            rooms.append(new_room.__dict__)
            with open(FILE_PATH, 'w+', encoding='utf-8') as f:
                json.dump(rooms, f)
            res = new_room.room_id
        return res

    def remove_room(self, room_id):
        '''Elimina el cliente seleccionado por el id'''
        encontrado = False
        rooms = self.get_all_rooms()
        for n_rooms in rooms:
            if n_rooms["room_id"] == room_id:
                rooms.remove(n_rooms)
                encontrado = True
        with open(FILE_PATH, 'w+', encoding='utf-8') as f:
            json.dump(rooms, f)
        if encontrado:
            res = f"room {room_id} deleted"
        else:
            res = f"room {room_id} not found"
        return res

    def show_room(self, room_id):
        '''Muetra el cliente seleccionado por el id'''
        res = None
        rooms = self.get_all_rooms()
        if len(rooms) > 0:
            for n_rooms in rooms:
                if n_rooms["room_id"] == room_id:
                    res = f"ID:{n_rooms['room_id']} price:{n_rooms['price']}"
        if res is None:
            res = f"room {room_id} not found"
        return res

    def get_all_rooms(self):
        '''Obiene todos los clietes del arhivo json'''
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as f:
                res = json.load(f)
                return res
        except FileNotFoundError:
            return []
