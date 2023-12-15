class Aircraft:
    def __init__(self, name=None, type=None, manufacturer=None, seat_count=None):
        self.name = name
        self.type = type
        self.manufacturer = manufacturer
        self.seat_count = seat_count

    def attribute_implementation(self, attributes_list):
        self.name = attributes_list[0]
        self.type = attributes_list[1]
        self.manufacturer = attributes_list[2]
        self.seat_count = attributes_list[3]