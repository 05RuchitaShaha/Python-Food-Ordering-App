# from _4_user_register_and_login import *
from _5_users_choices import *

class final:
    def execution(self, option, task):
        if option == 1:
            print("\n~ Get the Menu Card ~")
            task.menu_card()

        if option == 2:
            print("\n~ Place New Order ~")
            task.place_new_order()

        if option == 3:
            print("\n~ Review the Order History ~")
            task.order_history()

        if option == 4:
            print("\n~ Update Profile ~")
            task.update_profile()

        if option == 5:
            print("\n~ Visit Again ~\n")
            print("** Dear customer, we extend our gratitude towards you for your kind visit. **\n** We welcome your suggesstions, never hesitate to do so. **\n** DO VISIT AGAIN !! **\nThAnK YoU !")
            task.next_visit()

if __name__ == "__main__":
    task = user()
    main = final()

    while True:
        option = int(input("\nEnter the Number to :\n1.Get Menu \n2.Place Order \n3.Get Order History \n4.Update Profile\n5.Visit Again\n"))
        main.execution(option,task)
        if choice == 5:
            break
