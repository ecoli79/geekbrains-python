# lesson-8 example 3
# working with Excetion create own exception

class CheckListElement(Exception):
    def __init__(self, txt):
        self.error_text = txt


list_dig = []

while True:

    in_data = input(
        "Enter digit for insert to list, when you want finish enter 'stop': ")

    if in_data != "stop":
        try:
            if in_data.isdigit():
                list_dig.append(int(in_data))
            else:
                raise CheckListElement(f"{in_data} not a digit")
        except Exception as err:
            print(err)
    else:
        print(list_dig)
        break
