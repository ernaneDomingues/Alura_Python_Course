class Account:

    def __int__(self, name, account, balance, limit):
        self.__name = name
        self.__account = account
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print(f'Balance: {self.__balance}')

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__check_balance(value):
            self.__balance -= value
            print('Withdrawal successful.')
        else:
            print('Insufficient balance.')

    def transfer(self, value, destiny):
        if self.__check_balance(value):
            self.withdraw(value)
            destiny.deposit(value)
            print('Transfer successful.')
        else:
            print('Insufficient balance')

    def __check_balance(self, withdrawal):
        balance_available = self.__balance + self.__limit
        return withdrawal <= balance_available

    @property
    def balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit

    @staticmethod
    def bank_code():
        return '001'