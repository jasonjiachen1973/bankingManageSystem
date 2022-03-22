class AccountInfo(object):
    def __init__(self, name, password, balance=0):
        self.name = name
        self.password = password
        self.balance = balance

    def __str__(self):
        return f'{self.name},{self.password},{self.balance}'


