class Room:
    def __init__(self, rid, price):
        self.rid = rid
        self.price = price
        self.is_booked = False


class Customer:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.rooms = []


class Hotel:
    def __init__(self):
        self.rooms = {}
        self.customers = {}

    def add_room(self, room):
        self.rooms[room.rid] = room

    def add_customer(self, customer):
        self.customers[customer.cid] = customer

    def book(self, cid, rid):
        if cid in self.customers and rid in self.rooms:
            room = self.rooms[rid]
            if not room.is_booked:
                room.is_booked = True
                self.customers[cid].rooms.append(rid)
