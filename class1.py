# todo:
#  car class ---> mark, color, id(id reg) +
#  car object create with static function and return +
#  all car objects storage it anywhere +
#  function add / delete for id

class Garage:
    def __init__(self, all_cars):
        self.all_cars = all_cars

    all_cars = {}

    @classmethod
    def car_add(cls):
        try:
            c_id = int(input("id: "))
            color = input("Color: ")
            mark = input("Mark")
            Garage.all_cars[c_id] = [color, mark]
        except ValueError:
            pass

    @classmethod
    def print_cars(cls):
        print(Garage.all_cars)

    @classmethod
    def car_delete(cls, c_id):
        found = False
        for i in Garage.all_cars:
            if c_id == i:
                found = True

        if found:
            Garage.all_cars.pop(c_id)
            print("deleted")
        else:
            print("This car does not exit")


while True:
    a = int(input("Add car 1 / Show garage 2 / Delete car by id 3 / exit 4 "))
    if a == 1:
        Garage.car_add()
    elif a == 2:
        Garage.print_cars()
    elif a == 3:
        Garage.car_delete(int(input()))
    elif a == 4:
        exit()
