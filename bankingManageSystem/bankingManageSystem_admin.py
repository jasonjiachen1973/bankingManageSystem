from bankingManageSystem_user import *


class BankingManageSystemAdmin(BankingManageSystemUser):

    def run(self):
        # 1.1 load account data from file
        left_times = 0
        password_correct = False
        while left_times < 3:
            admin_password = int(input('Please enter your admin password: '))
            if admin_password == 123456:

                password_correct = True
                self.load_account_info()
                while True:
                    # 1.2 display function menu
                    self.show_menu()
                    # 1.3 user input function number
                    menu_num = int(input('Please select function number: '))
                    # 1.4 perform function according the number input
                    if menu_num == 1:
                        # All account holder list with details
                        self.all_account_list()

                    elif menu_num == 2:
                        # Modify Account
                        self.modify_account()
                    elif menu_num == 3:
                        # Close Account
                        self.close_account()
                    elif menu_num == 4:
                        # quit system
                        self.save_data()
                        left_times = 3
                        break
                    else:
                        print('Please enter valid number!')
            else:
                print('password is incorrect ! ')
                left_times += 1



        # 2.1 display function menu

    @staticmethod
    def show_menu():
        print('Please select the function below:')
        print('1: All account holder list with details')
        print('2: Modify Account ')
        print('3: Close Account')
        print('4: quit')

    def all_account_list(self):
        print('%-20s\t\t%-20s\t\t%-20s' % ('name', 'password', 'balance'))

        for i in self.account_info_list:
            print('%-20s\t\t%-20s\t\t%-20s'%(i.name, i.password, i.balance))


        # BankingManageSystemUser.__init__(self)
        # print(self.account_info_list)

    def modify_account(self):

        name_input = input('Please enter the account name you want to modify: ')
        user_exist = False
        for i in self.account_info_list:
            if i.name == name_input:
                while True:
                    print('Available options: ')
                    print('1: name')
                    print('2: password')
                    print('3: balance')
                    print('4: quit')

                    num_input = int(input('Please enter the number of selection: '))
                    if num_input == 1:
                        new_name = input('Please enter the new name')
                        i.name = new_name
                    elif num_input ==2:
                        new_password = input('Please enter the new password')
                        i.password = new_password
                    elif num_input == 3:
                        new_balance = input('Please enter the new balance')
                        i.balance = new_balance
                    elif num_input == 4:
                        break
                    else:
                        print('Please enter valid number!')

    def close_account(self):
        name_exist = False
        while True:
            name_input = input('Please enter the account name you want to close(enter e to quit: ')
            for i in range(len(self.account_info_list)-1):
                if name_input == self.account_info_list[i].name:
                    del self.account_info_list[i]
                    name_exist = True
                    break
            if name_input == 'e':
                break
            if not name_exist:
                print('The name is not exist!')






