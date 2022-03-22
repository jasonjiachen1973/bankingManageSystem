from bankingManageSystem_user import *
from bankingManageSystem_admin import *

if __name__ == '__main__':
    while True:
        print('Welcome to use banking management system:')
        print('1: general user')
        print('2: admin  ')
        print('3: quit  ')
        logging_menu_num = int(input('Please select account type: '))

        if logging_menu_num == 1:
            account_user = BankingManageSystemUser()
            account_user.run()
        elif logging_menu_num ==2:
            account_admin = BankingManageSystemAdmin()
            account_admin.run()
        elif logging_menu_num == 3:
            print('Thanks for using, goodbye!')
            break
        else:
            print('Please choose 1 or 2')


