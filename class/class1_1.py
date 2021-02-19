# todo:
#  car class ---> mark, color, id(id reg) +
#  car object create with static function and return +
#  all car objects storage it anywhere +
#  function add / delete for id


class Garage:
    def __init__(self):
        self.all_cars = {}

    def car_add(self):

        try:
            c_id = int(input("id: "))
            mark = input("Mark")
            color = input("Color: ")
            self.all_cars[c_id] = [color, mark]

        except ValueError:
            pass

    def print_cars(self):
        print(self.all_cars)

    def car_delete(self, c_id):
        found = False
        for i in self.all_cars:
            if c_id == i:
                found = True

        if found:
            self.all_cars.pop(c_id)
            print("deleted")
        else:
            print("This car does not exit")


garage = Garage()
while True:

    a = int(input("Add car 1 / Show garage 2 / Delete car by id 3 / exit 4 "))
    if a == 1:
        garage.car_add()
    elif a == 2:
        garage.print_cars()
    elif a == 3:
        garage.car_delete(int(input("")))
    elif a == 4:
        exit()
