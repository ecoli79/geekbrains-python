# lesson-8 example 2
# working with Exception creare own class

class DevByZero(Exception):
    def __init__(self, txt):
        self.error_text = txt


while True:
    try:
        in_data = int(input("imput number: "))
        if in_data == 0:
            raise DevByZero("Attention! Devezion by Zero!")

        res = 6 // in_data

    except Exception as err:
        print(err)

    else:
        print(res)
