# lesson-6 examaple 2
# working with class initialization class new commit

class Road():
    """
    Класс дорога

    аттрибуты класса:
    length - длина дороги в метрах, обязательный атрибут при создании объекта класса Road
    width - ширина дороги в метрах, обязательный атрибут при создании объекта класса Road
    """
    _length = int()
    _width = int()

    def __init__(self, length, width):

        try:
            self._length = int(length)
            self._width = int(width)
        except Exception as err:
            print(err)

    def count_ashpalt(self):

        mass_asphalt = self._length * self._width * 25 * 5
        print(
            f"Масса асфальтра необхимого для покрытия дорожного полотна составляет: {round(mass_asphalt / 1000)} килограмм.")


road_m4 = Road(1250000, 60)
road_m4.count_ashpalt()
