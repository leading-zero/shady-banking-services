import sys
import backend


class FrontEnd:

    # The get_str method displays the prompt argument and
    # checks to see if the input is empty. If the input is empty the
    # user is asked to resubmit their selection.

    # The entered_str variable could be renamed something like "user_input"
    # however I think that entered_str is equally descriptive.

    def get_str(prompt):
        sys.stdout.write(prompt)
        entered_str = sys.stdin.readline().strip()
        if entered_str == "":
            raise ValueError("\nInput cannot be empty.\n"
                             "Re-enter: ")
        return entered_str

    # The get_int method attempts to turn the prompt argument into an integer.
    # If a number is not entered the user is asked to enter a number.

    # Similar to entered_str in the get_str method, the value variable could be
    # renamed something like user_input but I think value is more suitable as
    # the word 'value' is generally associated with a numeric value.

    def get_int(prompt):
        value = None
        while value == None:
            try:
                value = int(FrontEnd.get_str(prompt))
            except:
                raise TypeError("Please enter a number.\n")
        return value

    # The get_float method attempts to turn the prompt argument into an integer.
    # If a number is not entered the user is asked to enter a number.

    # Similar to entered_str in the get_str method, the value variable could be
    # renamed something like user_input but I think value is more suitable as
    # the word 'value' is generally associated with a numeric value.

    def get_float(prompt):
        value = None
        while value == None:
            try:
                value = float(FrontEnd.get_str(prompt))
            except:
                raise TypeError("Please enter a number.\n")
        return value

    # The check_account_pin method turns the user's input into a string and
    # checks to see if the length of that string is less than 4 digits. If the
    # account_pin is less than four digits in length the user is asked to
    # resubmit a pin number that is four or more digits. When that condition is
    # satisfied the account_pin is returned.

    def check_account_pin(account_pin):
        if len(str(account_pin)) < 4:
            raise ValueError("PIN must be 4 or more digits.")
        return account_pin

    # Initialise the FrontEnd object

    def __init__(self):

        # This variable initialises the backend and passes in data.csv as an
        # argument to load existing accounts in that file.
        self.backend = backend.BackEnd("data.csv")

        # This line prints the number of accounts that were loaded from data.csv

        sys.stdout.write(
            "\n" +
            str(self.backend.get_acc_count()) +
            " accounts loaded.\n"
        )

        # The menu variable presents the user with a list of options they can
        # select from.

        # I think the naming of the menu variable is self explanatory and as
        # such, using another name for it would be less descriptive in regards
        # to it's function.

        menu = "----------------------\n"
        menu += "$hady Banking $ervices\n"
        menu += "----------------------\n"
        menu += "[C]reate an account\n"
        menu += "[A]ccount balance\n"
        menu += "[W]ithdraw funds\n"
        menu += "[D]eposit funds\n"
        menu += "[S]ave accounts\n"
        menu += "E[x]it\n"

        # print the menu on the screen

        sys.stdout.write(menu)

        # The selection variable is used to match the user's input with the
        # selections available in the menu.

        # Other names for this variable could be synonymous with "selection"
        # such as "choice". I've opted to use "selection" but "choice" would be
        # equally valid.

        selection = None

        # The following code block passes the user selection to the get_str
        # method. If the input is empty an exception is raised and the user is
        # asked to re-enter their selection.

        while selection == None:
            try:
                selection = FrontEnd.get_str("Enter selection: ")
            except Exception as e:
                sys.stderr.write(str(e))

        # The following while loop matches the value of the selection variable
        # and executes the appropriate statement when a match is found. If the
        # user enters "x" the program will end.

        while selection != "x":
            sys.stdout.write("\n")

            # This code block creates a new account.
            #
            # As this application emulates established banking concepts that
            # most people would be familiar with I've used the following
            # variable names for each account:
            #
            # account_number
            # account_pin
            # account_name
            # account_balance
            #
            # These variables could omit the account_ prefix however I think
            # having it present makes the variables a little more descriptive
            # and consistent. Variations on these names would make things
            # unnecessarily confusing.

            if selection == "c":
                sys.stdout.write("------------------\n")
                sys.stdout.write("Create an account:\n")
                sys.stdout.write("------------------\n")

                # set account_name to None and then pass to get_str to check if
                # the string is empty.

                account_name = None
                while account_name == None:
                    try:
                        account_name = FrontEnd.get_str("Enter account name: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # Generate the account number using the get_random_acc_no method
                # in the backend.

                account_number = self.backend.get_random_acc_no()
                sys.stdout.write("\n")
                sys.stdout.write("Generating account number...")
                sys.stdout.write("\n")
                sys.stdout.write("Your account number is: " +
                                 str(account_number) + "\n")

                # set account_pin to None and then pass to get_int to check if
                # the input is a number. If the input is not empty and a number,
                # then pass account_pin to the check_account_pin method to check
                # if the account_pin is longer than 4 digits.

                account_pin = None
                while account_pin == None:
                    try:
                        check_account_pin = FrontEnd.get_int("Enter PIN: ")
                        account_pin = FrontEnd.check_account_pin(
                            check_account_pin)
                    except Exception as e:
                        sys.stderr.write(str(e))
                sys.stdout.write("\n")

                # set the deposit_amount to None and pass to get_str to check if
                # the string is empty.

                deposit_amount = None
                while deposit_amount == None:
                    try:
                        deposit_amount = FrontEnd.get_int(
                            "Please enter a deposit amount in whole dollars: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # The account_balance variable passes the deposit_amount
                # variable to the init_deposit mehtod in the backend to
                # calculate the account balance after Shady Banking takes their
                # cut of the deposit amount.

                account_balance = self.backend.init_deposit(deposit_amount)

                # Create the account using the create_account method in the
                # backend.

                self.backend.create_account(account_number,
                                            account_pin,
                                            account_name,
                                            account_balance)

                sys.stdout.write("\n")

                # The following message is displayed to the user after the
                # account is successfully created. I think the variable name is
                # suitable here as something like success_message would mean
                # having less characters to use before hitting the 80 column
                # limit.

                message = "Account created successfully.\n\n"
                message += "Your new account details are listed below:\n"
                message += "Account Number: " + str(account_number) + "\n"
                message += "Account Name: " + account_name + "\n"
                message += "Account PIN: " + str(account_pin) + "\n"
                message += "Account Balance: $" + str(account_balance) + "\n\n"
                message += "Thanks for using Shady Banking Services\n\n"

                sys.stdout.write(message)

            # this code block will ask the user to enter their account name
            # and PIN code, then display their account balance.

            elif selection == "a":
                sys.stdout.write("---------------\n")
                sys.stdout.write("Account balance\n")
                sys.stdout.write("---------------\n")

                # set account_pin to None and then pass to get_int to check if
                # the string is a number.

                account_pin = None
                while account_pin == None:
                    try:
                        account_pin = FrontEnd.get_int("Enter PIN: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # set account_name to None and then pass to get_str to check if
                # the string is empty.

                account_name = None
                while account_name == None:
                    try:
                        account_name = FrontEnd.get_str("Enter account name: ")
                    except Exception as e:
                        sys.stderr.write(str(e))
                sys.stdout.write("\n")

                # The following code block passes the account_pin and
                # account_name to the get_account method in the backend. If a
                # match is made, it will display the account balance for the
                # account that details have been provided for. If no match is
                # made, the user is advised the account details were incorrect
                # and to attempt the transaction again.

                if self.backend.get_account(account_pin, account_name):
                    sys.stdout.write("You have $" +
                                     str(self.backend.account_balance(
                                         account_pin,
                                         account_name))
                                     + " in your account.\n")
                else:
                    sys.stdout.write(
                        "Incorrect account details. Please try again.\n")

            # this code block will ask the user to enter their account name
            # and PIN code, then ask how much they would like to withdraw
            # from their account. The withdrawal_amount is then subtracted from
            # the account matching the account_name and account_pin provided.

            elif selection == "w":
                sys.stdout.write("--------------\n")
                sys.stdout.write("Withdraw Funds\n")
                sys.stdout.write("--------------\n")

                # set account_pin to None and then pass to get_int to check if
                # the input is a number.

                account_pin = None
                while account_pin == None:
                    try:
                        account_pin = FrontEnd.get_int("Enter PIN: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # set account_name to None and then pass to get_str to check if
                # the string is empty.

                account_name = None
                while account_name == None:
                    try:
                        account_name = FrontEnd.get_str("Enter account name: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # set withdrawal_amount to None and pass to get_int to check if
                # the input is a number.

                withdrawal_amount = None
                while withdrawal_amount == None:
                    try:
                        withdrawal_amount = FrontEnd.get_int(
                            "Please enter a withdrawal amount in whole dollars: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # this code block passes the account_pin, account_name and
                # withdrawal_amount to the withdrawal method in the backend. If
                # the details are matched successfully, the withdrawal amount is
                # subtracted from the account's balance and the updated account
                # balance is displayed back to the user. If no match is
                # made, the user is advised the account details were incorrect
                # and to attempt the transaction again.

                if self.backend.withdrawal(account_pin,
                                           account_name,
                                           withdrawal_amount):

                    sys.stdout.write(
                        "Thanks for using Shady Banking.\n"
                        "You have $" +
                        str(self.backend.account_balance(account_pin,
                                                         account_name)) +
                        " remaining in your account.\n")

                else:
                    sys.stdout.write(
                        "Invalid account details. Please try again.\n"
                    )

            # this code block will ask the user to enter their account name
            # and PIN code, then ask how much they would like to deposit to
            # their account.
            elif selection == "d":
                sys.stdout.write("-------------\n")
                sys.stdout.write("Deposit Funds\n")
                sys.stdout.write("-------------\n")

                # set account_pin to None and then pass to get_int to check if
                # the input is a number.

                account_pin = None
                while account_pin == None:
                    try:
                        account_pin = FrontEnd.get_int("Enter PIN: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # set account_name to None and then pass to get_str to check if
                # the string is empty.

                account_name = None
                while account_name == None:
                    try:
                        account_name = FrontEnd.get_str("Enter account name: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # set deposit_amount to None and pass to get_int to check if
                # the input is a number.

                deposit_amount = None
                while deposit_amount == None:
                    try:
                        deposit_amount = FrontEnd.get_int(
                            "Please enter a deposit amount in whole dollars: ")
                    except Exception as e:
                        sys.stderr.write(str(e))

                # this code block passes the account_pin, account_name and
                # deposit_amount to the deposit method in the backend. If
                # the details are matched successfully, the deposit amount is
                # added to the account's balance and the updated account
                # balance is displayed back to the user. If no match is
                # made, the user is advised the account details were incorrect
                # and to attempt the transaction again.

                if self.backend.deposit(account_pin,
                                        account_name,
                                        deposit_amount):

                    account_balance = str(self.backend.account_balance(
                        account_pin,
                        account_name))

                    sys.stdout.write(
                        "Thanks for using Shady Banking.\n"
                        "You have $" + account_balance +
                        " remaining in your account.\n")

                else:
                    sys.stdout.write(
                        "Invalid account details. Please try again.\n"
                    )

            # The following code block will attempt to save the account data by
            # calling the save_data method in the backend. After writing the
            # data to the file, the user is advised on how many accounts were
            # written to the file. If the file was unable to be written to, the
            # user is notified and asked to try again.

            elif selection == "s":
                try:
                    self.backend.save_data()
                    sys.stdout.write("Saving account data...\n")
                    sys.stdout.write(
                        str(self.backend.get_acc_count()) +
                        " accounts saved to file.\n")
                except:
                    sys.stderr.write("Unable to save to file.\n"
                                     "Please try again.\n")

            # This else statement will advise the user that their selection
            # did not match a selection from the menu.

            else:
                sys.stderr.write("Invalid selection.\n")

            sys.stdout.write(menu)
            selection = FrontEnd.get_str("Enter selection: ")


# create FrontEnd object
run_shady_banking = FrontEnd()
