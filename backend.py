import random


class BackEnd:

    # initialise BackEnd
    def __init__(self, filename):

        # This variable is used to store account data created by the
        # create_account method. This variable could be named __account_list but
        # I prefer this shortened name.

        self.__accounts = []

        # This variable is used to store the filename passed from the frontend
        # when FrontEnd is initialised. This variable could be named something
        # like save_file or similar.

        self.__accounts_filename = filename

        # file point variable
        fp = None

        # attempt to open the file in self.__accounts_filename. If the file is
        # not able to be loaded then save a file with the provided filename.
        try:
            fp = open(self.__accounts_filename)

        except:
            self.save_data()

        if fp != None:
            self.load_data(self.__accounts_filename)

    # This method returns the length of the self.__accounts variable to indicate
    # if data is present.

    def get_acc_count(self):
        return len(self.__accounts)

    # The create_account method will take the details passed in from the create
    # the FrontEnd and then pass those details to the self.__accounts
    # variable to store the account information.

    def create_account(self,
                       account_number,
                       account_pin,
                       account_name,
                       account_balance):

        self.__accounts.append(Account(account_number,
                                       account_pin,
                                       account_name,
                                       account_balance))

    # The get_random_acc_no method randomly generates an account number to
    # associate with a newly created account and then returns it for further
    # use in the frontend.

    def get_random_acc_no(self):

        # the start_number & end_number variables determine the range from which
        # account numbers will be selected.
        #
        # Alternatively these variables could be called something like
        # low_number & high_number to indicate the range from which account
        # numbers will be selected. I think they're readily interchangeable so
        # don't really see the benefit of using one over the other.

        start_number = 10000000
        end_number = 100000001

        # The account number variable then uses the randrange function to
        # produce an account number within the range of the start_number &
        # end_number variables.

        account_number = int(random.randrange(start_number, end_number))

        return account_number

    # The get_account method is used to match the account_pin and account_name
    # input by the user with the existing accounts in the self.__accounts list.

    def get_account(self,
                    account_pin,
                    account_name):

        # found_account is set to None and populated with matching account
        # details after running the below while loop. This variable could be
        # alternatively named something like matched_account but I think the two
        # are similar in meaning so readily interchangeable.

        found_account = None

        # this variable's value is set by running the get_acc_count method. The
        # name of this variable and it's function is pretty obvious and
        # variations on it such as length_of_accounts would be needlessly wordy.

        len_accounts = self.get_acc_count()

        i = 0

        # The following while loop attempts to match the account_pin and
        # account_name input by the user with existing accounts in the
        # self.__accounts list. When a match is found the found_account variable
        # is updated with the details of the matching account and returned for
        # further use.

        while i < len_accounts and \
                self.__accounts[i].is_equals(account_pin, account_name) \
                == False:
            i += 1

        if i < len_accounts:
            found_account = self.__accounts[i]

        return found_account

    # The account_balance method returns the account balance for the account
    # that matches the account_pin and account_name input by the user. The
    # account balance is then returned for further use in the frontend.

    def account_balance(self, account_pin, account_name):
        target_account = self.get_account(account_pin, account_name)
        balance = target_account.account_balance

        return balance

    # The withdrawal and deposit methods are used to add and subtract funds from
    # an account. After the account_pin and account_name are matched to an
    # account, the transaction is performed on the account_balance. In both
    # methods the success variable is updated to True and returned to the if
    # statement in the frontend to confirm that the transaction has been carried
    # out successfully.

    def withdrawal(self,
                   account_pin,
                   account_name,
                   withdrawal_amount
                   ):

        success = False
        target_account = self.get_account(account_pin, account_name)

        if target_account != None:
            account_balance = float(
                self.account_balance(account_pin, account_name))

            # Shady Banking transaction fee
            txn_fee = withdrawal_amount / 10

            # calculate account balance and apply transaction fee.
            updated_balance = account_balance - withdrawal_amount - txn_fee

            # update user account balance
            target_account.account_balance = updated_balance
            success = True

        return success

    def deposit(self,
                account_pin,
                account_name,
                deposit_amount
                ):

        success = False
        target_account = self.get_account(account_pin, account_name)

        if target_account != None:
            account_balance = float(
                self.account_balance(account_pin, account_name)
            )

            # Shady Banking transaction fee
            txn_fee = deposit_amount / 10

            # calculate account balance and apply transaction fee.
            updated_balance = account_balance + deposit_amount - txn_fee

            # update user account balance
            target_account.account_balance = updated_balance
            success = True

        return success

    # The init_deposit method is used to calculate the account's balance after
    # Shady Banking takes their transaction fee. The account balance is then
    # returned.

    def init_deposit(self, deposit_amount):
        txn_fee = deposit_amount / 10
        account_balance = deposit_amount - txn_fee
        return account_balance

    # The save_data method is used to write the self.__accounts list to the file
    # in the self.__accounts_filename variable.

    def save_data(self):
        # open the file
        fp = open(self.__accounts_filename, "w")
        # write to the file
        fp.write(str(self))
        # close the file
        fp.close()

    # The load_data method is used read from the filename passed into the
    # method. It then splits the data at each comma and passes each segment to
    # the create_account method.

    def load_data(self, filename):

        file_object = open(filename, "r")
        i = 0
        line = file_object.readline()

        while line != "":
            field = line.split(",")
            account_number = int(field[0])
            account_pin = int(field[1])
            account_name = field[2]
            account_balance = float(field[3])
            BackEnd.create_account(self,
                                   account_number,
                                   account_pin,
                                   account_name,
                                   account_balance)
            line = file_object.readline()
            i += 1
            file_object.close()

    def __str__(self):
        len_accounts = self.get_acc_count()
        summary = ""
        i = 0
        while i < len_accounts:
            summary += str(self.__accounts[i]) + "\n"
            i += 1
        return summary


class Account:

    # initialise Account object

    def __init__(self,
                 account_number,
                 account_pin,
                 account_name,
                 account_balance):
        self.__account_number = account_number
        self.__account_pin = account_pin
        self.__account_name = account_name
        self.__account_balance = account_balance

    # accessor for account name
    @property
    def account_name(self):
        return self.__account_name

    # accessor for account number
    @property
    def account_number(self):
        return self.__account_number

    # accessor for account pin
    @property
    def account_pin(self):
        return self.__account_pin

    # accessor for account balance
    @property
    def account_balance(self):
        return self.__account_balance

    # mutator for balance
    @account_balance.setter
    def account_balance(self, account_balance):
        self.__account_balance = account_balance

    # the is_equals method checks to see if the account name and pin input by
    # the user matches the
    def is_equals(self, account_pin, account_name):
        outcome = False

        if self.__account_pin == account_pin and \
                self.__account_name == account_name:
            outcome = True
        return outcome

    # the __str__ method returns a summary of the account details
    def __str__(self):
        summary = str(self.__account_number) + ","
        summary += str(self.__account_pin) + ","
        summary += str(self.__account_name) + ","
        summary += str(self.__account_balance)

        return summary
