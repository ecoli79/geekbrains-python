# lesson-6 example 4
# working with classes new commit

class Car():
    """
    базовый класс Car

    speed - скорость автомобиля
    color - цвет автомобиля
    name - название автомобиля
    is_police - принадлежность к автомобилям полиции
    """

    speed = 0
    color = ""
    name = ""
    is_police = False
    status_go = bool
    status_stop = bool
    direction = ""

    def __init__(self, color, name, speed=0, is_polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def show_speed(self):
        """
        метод показывающий скорость авто
        """
        print(f"{self.name} движется со скоротью {self.speed} км/ч")

    def go(self):
        """
        метод сообщающий что машина поехала
        """
        if self.status_go:
            print(f"{self.name} поехала!")

    def stop(self):
        """
        метод сообщающий что машина остановилась
        """
        if self.status_stop:
            print(f"{self.name} остановилась!")

    def turn(self, direction):
        """
        метод сообщающий что машина повернула

        direction is a string "turn_left, turn_right"
        """
        self.direction = direction

    def turn_direction(self):
        """
        метод сообщающий куда повернула машина
        """
        print(f"{self.name} - {self.direction}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(
                f"Внимание! {self.name} превышает допустимую скорость движения на {self.speed - 60} км/ч.")
        else:
            print(f"{self.name} движется со скоротью {self.speed} км/ч")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(
                f"Внимание! {self.name} превышает допустимую скорость движения на {self.speed - 40} км/ч.")
        else:
            print(f"{self.name} движется со скоротью {self.speed} км/ч")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


sportcar = SportCar("RedBlue", "Porshe911TurboS", 210)
golfcar = TownCar("White", "Golf", 80)
buldozer = WorkCar("Yellow", "Buldozer", 60)
policemancar = PoliceCar("BlueAndWhite", "Buhanka", 110, True)

sportcar.turn("turn_right")
golfcar.turn("turn_left")
buldozer.turn("turn_right")
policemancar.turn("forward")

sportcar.status_go = True
golfcar.status_go = False
buldozer.status_go = False
policemancar.status_go = True

sportcar.status_stop = False
golfcar.status_stop = True
buldozer.status_stop = True
policemancar.status_stop = False

cars_of_town = {sportcar, golfcar, buldozer, policemancar}

print(f"В районом центре Гарцы всего {len(cars_of_town)} машины. Среди них:")
for car in cars_of_town:
    print(f"{car.name} {car.color} цвета.")

print("-" * 45)
for car in cars_of_town:
    if car.is_polise:
        print(f"Полицеская машина {car.name} патрулирует улицы")

print("-" * 45)
print("Какие из машин сейчас в пути: ")
for car in cars_of_town:
    if car.status_go:
        car.go()

print("-" * 45)
print("Какие машины сейчас не двигаются: ")
for car in cars_of_town:
    if car.status_stop:
        car.stop()

print("-" * 45)
print("Направление движения автомобилей: ")
for car in cars_of_town:
    car.turn_direction()
