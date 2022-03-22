from account_info import *


class BankingManageSystemUser(object):
    def __init__(self):
        # list to store data
        self.account_info_list = []

    # 1 program entry function
    def run(self):
        # 1.1 load account data from file
        self.load_account_info()
        print( self.account_info_list)
        while True:
            # 1.2 display function menu
            self.show_menu()
            # 1.3 user input function number
            menu_num = int(input('Please select function number: '))
            # 1.4 perform function according the number input
            if menu_num == 1:
                # create new account
                self.create_account()
            elif menu_num == 2:
                # deposit amount
                self.deposit()
            elif menu_num == 3:
                # withdraw amount
                self.withdraw()
            elif menu_num == 4:
                # balance enquiry
                self.balance_enquiry()
            elif menu_num == 5:
                # quit system
                self.save_data()
                break
            else:
                print('Please enter valid number!')


    # 2 system functional function
    # 2.1 display function menu
    @staticmethod
    def show_menu():
        print('Please select the function below:')
        print('1: create new account')
        print('2: deposit')
        print('3: withdraw')
        print('4: balance enquiry')
        print('5: quit')

    # 2.2 create account
    def create_account(self):
        # 1 enter name. password
        name = input('Please enter your name: ')
        password = input('Please enter your password: ')

        # 2 create account_info object ( import account_info module first)
        account_info = AccountInfo(name,password)
        # 3 add account_info object to a list
        self.account_info_list.append(account_info)
        # 4 print information
        print('your name: ', account_info.name)
        print('your passwor:', account_info.password)
        print('your balance: ', account_info.balance)

    # 2.3 deposit
    def deposit(self):
        # print('deposit amount')
        name_input = input('Please enter your name: ')
        user_exist = False
        for i in self.account_info_list:
            if i.name == name_input:
                while True:
                    password = input('Please enter your password: ')
                    if i.password == password:
                        deposit_amount = int(input('Please enter deposit amount: '))
                        i.balance += deposit_amount
                        print('your current balance is :', i.balance)
                        user_exist = True
                        break
                    else:
                        print('password is incorrect!')
        if not user_exist:
            print('username does not exist! ')

    # 2.4 withdraw
    def withdraw(self):
        # print('withdraw')

        name_input = input('Please enter your name: ')
        user_exist = False
        for i in self.account_info_list:
            if i.name == name_input:
                withdraw_finish = False
                while not withdraw_finish:
                    password = input('Please enter your password: ')
                    if i.password == password:
                        while True:
                            withdraw_amount = int(input('Please enter withdraw amount: '))
                            if withdraw_amount < i.balance:
                                i.balance -= withdraw_amount
                                print('your current balance is :', i.balance)
                                withdraw_finish = True
                                user_exist = True
                                break
                            else:
                                print('Insufficient balance!')
                                print('your current balance is :', i.balance)
                    else:
                        print('password is incorrect!')

        if not user_exist:
            print('username does not exist! ')

    # 2.5 balance_enquiry
    def balance_enquiry(self):
        # print('Return enquiry result')
        name_input = input('Please enter your name: ')
        user_exist = False
        for i in self.account_info_list:
            if i.name == name_input:
                while True:
                    password = input('Please enter your password: ')
                    if i.password == password:

                        print('your current balance is :', i.balance)
                        user_exist = True
                        break
                    else:
                        print('password is incorrect!')

        if not user_exist:
                print('username does not exist! ')
    # save_data

    def save_data(self):

        # requirement : save data to file after modifying
        # 1 open file
        f = open('account_info.data', 'w')
        # 2 write data to file
        # note 1: you cannot save the memory address of the object, so need to convert it to list of dictionary
        new_list = [i.__dict__ for i in self.account_info_list]
        # print(new_list)
        # note 2: need to convert data type to string to save to file
        f.write(str(new_list))

        # 3 close file
        f.close()

    def load_account_info(self):
        # try to open file , if file does not exist ,create a new file, else read data from file
        try:
            f = open('account_info.data', 'r')
        except:
            f = open('account_info.data', 'w')
        else:
            # 1 read data
            data = f.read()
            # 2 the data read from file is string in which is dictionary so need to convert it object to store in list
            new_list = eval(data)
            self.account_info_list = [AccountInfo(i['name'],i['password'], i['balance']) for i in new_list]




