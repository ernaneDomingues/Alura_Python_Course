import re

class MobileValidation:
    def __init__(self, mobile_number):
        if self.number_validation(mobile_number):
            self.cellphone_number = mobile_number
        else:
            raise ValueError('Inalid mobile number!')

    def __str__(self):
        return self.number_format()

    def number_validation(self, mobile_number):
        default = "([0-9]{1,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        response = re.findall(default, mobile_number)
        if response:
            return True
        else:
            return False

    def number_format(self):
        default = "([0-9]{1,3})?([0-9]{2})([0-9]{5})([0-9]{4})"
        response = re.search(default, self.cellphone_number)
        if response.group(1):
            return f'+{response.group(1)} ({response.group(2)}) {response.group(3)}-{response.group(4)}'
        else:
            return f'({response.group(2)}) {response.group(3)}-{response.group(4)}'