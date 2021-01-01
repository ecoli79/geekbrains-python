# lesson 6 example 1
# working with classes new commit

# colorama import для выделения цветом текста в консоли python

import time
import os
from colorama import Fore, Back, Style


class TrafficLight():

    color = ["red", "yellow", "green"]

    def running(self):
        while True:
            print(Fore.RED + "Trafficlight: {}".format(self.color[0]))
            time.sleep(7)
            os.system("cls||clear")
            print(Fore.YELLOW + f"TrafficLignt: {self.color[1]}")
            time.sleep(2)
            os.system("cls||clear")
            print(Fore.GREEN + f"TrafficLight: {self.color[2]}")
            time.sleep(9)
            os.system("cls||clear")


svetophor = TrafficLight()
svetophor.running()
