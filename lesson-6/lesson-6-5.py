# lesson-6 example 5
# working with classes new commit

class Stationery():

    title = ""

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, name):
        self.title = name

    def draw(self):
        print(f"The {self.title} draw bold line")


class Pencil(Stationery):
    def __init__(self, name):
        self.title = name

    def draw(self):
        print(f"The {self.title} draw think line")


class Handle(Stationery):
    def __init__(self, name):
        self.title = name

    def draw(self):
        print(f"The {self.title} draw very bold line")


my_pen = Pen("my_pen")
my_pencil = Pencil("my_pencil")
my_handle = Handle("my_handle")

my_pen.draw()
my_pencil.draw()
my_handle.draw()
