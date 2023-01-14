#Written by Emin Ayyıldız Hüseyin Berk Keskin
print("Written by Emin Ayyıldız Hüseyin Berk Keskin")

from enum import Enum
import time

class PaymentMethod(Enum):
    CREDIT_CARD = 1
    PAYPAL = 2
    CASH = 3

restaurant_table_list = {
    2: [{"reservation": None, "order_total": 0.0, "table_number": i} for i in range(1,11)],
    4: [{"reservation": None, "order_total": 0.0, "table_number": i} for i in range(11,21)],
    6: [{"reservation": None, "order_total": 0.0, "table_number": i} for i in range(21,31)]
}

def make_reservation():
    table_size = int(input("Enter the number of seating you want for the table (2-4-6): "))
    if table_size == 2:
        table_number = int(input("Enter the number of the table you want to reserve (1-10) : "))
    elif table_size ==4:
        table_number = int(input("Enter the number of the table you want to reserve (11-20) : "))
    elif table_size == 6:
        table_number = int(input("Enter the number of the table you want to reserve (21-30) : "))
    else:
        print("Invalid table size or table number")
        return

    reservatior_name= input("Enter the name for the reservation: ")
    print("Reservation confirming, Please wait...")
    time.sleep(1.5)
    if table_size in restaurant_table_list:
        available_table = None
        for table in restaurant_table_list[table_size]:
            if table["reservation"] is None and table["table_number"] == table_number:
                available_table = table
                break
        if available_table:
            available_table["reservation"] = reservatior_name
            print(f"Reservation for table number {available_table['table_number']} with seating {table_size} has been made under the name {reservatior_name}.")
        else:
            print(f"Sorry, the table number {table_number} is not available or it doesn't match with seating size")
    else:
        print(f"Sorry, we do not have a table that seats {table_size}.")



def check_availability():
    for table_size, table_data in restaurant_table_list.items():
        available_tables = 0
        for table in table_data:
            if table["reservation"] is None:
                available_tables += 1
        print(f"{available_tables} table with seating {table_size} are available.")

def make_order():
    
    
    menu_meal = {
        "Adana Kebap": 65.99,
        "Urfa Kebap": 70.00,
        "Hatay Dürüm": 55.00,
        "İskender": 75.99,
        "Beyti": 85.99,
        "Ayran": 15.00,
        "Şalgam": 20.00
    }
    print("Menu:")
    for item, price in menu_meal.items():
        print(f"{item} - {price} TL")
    order = input("Which item you want to order, Please enter name : ")

    if order in menu_meal:
        order_total = menu_meal[order]
        
    else:
        print("Invalid order")
        return
    
    reserved_table = None
    for table_size, table_data in restaurant_table_list.items():
        for table in table_data:
            if table["table_number"] == table_number:
                reserved_table = table
                break
        if reserved_table:
            break
    if reserved_table:
        if reserved_table["reservation"] is not None:
            reserved_table["order_total"] += order_total
            print(f"Order placed for table number {table_number}. Total is now {reserved_table['order_total']}")
            add_meal= input("Do you want to add more products (yes/no) :")
            if add_meal == "yes" or add_meal == "YES" or add_meal == "Yes":

                return make_order()
            elif add_meal == "no" or add_meal == "NO" or add_meal == "No":
                print("You are being redirected to the main menu, please wait...")
                time.sleep(1.5)

        else:
            print(f"Sorry, the table number {table_number} is not reserved.")
    else:
        print(f"Sorry, we do not have a table with number {table_number}.")


def pay_order():
    table_number = int(input("Enter the number of the table you want to make payment: "))
    
    reserved_table = None
    for table_size, table_data in restaurant_table_list.items():
        for table in table_data:
            if table["table_number"] == table_number:
                reserved_table = table
                break
        if reserved_table:
            break
    if reserved_table:
        if reserved_table["reservation"] is not None:
            order_total = reserved_table["order_total"]
            print(f"Total amount to be paid is {order_total} TL")
            for payment_method in PaymentMethod:
                print(payment_method.value, payment_method.name)
            selected_payment_method = int(input("--->"))
            if selected_payment_method == PaymentMethod.CREDIT_CARD.value:
                card_number = input("Enter your 16 digit card number : ")
                card_password = input("Enter your 4 digit card password  : ")
                if len(card_number) >= 15 and len(card_password) == 4:
                    print(f"{order_total} TL fee is provided from your bank, Please wait...")
                    time.sleep(1.5)
                    print(f"Payment of {order_total} TL received in cash for table number {table_number}. Table is now free.")
                    reserved_table["order_total"] = 0
                    reserved_table["reservation"] = None
                    

                else:
                    print("Invalid card number...")
            elif selected_payment_method == PaymentMethod.PAYPAL.value:
                paypal_card_number = input("Enter your 16 digit card number : ")
                paypal_card_password = input("Enter your 4 digit card password  : ")
                if len(paypal_card_number) >= 15 and len(paypal_card_password) == 4:
                    print(f"{order_total} TL fee is provided from your bank, Please wait...")
                    time.sleep(1.5)
                    print(f"Payment of {order_total} TL received by card for table number {table_number}. Table is now free.")
                    reserved_table["order_total"] = 0
                    reserved_table["reservation"] = None
                else:
                    print("Invalid card number...")
            elif selected_payment_method == PaymentMethod.CASH.value:
                print(f"Payment of {order_total} TL received by card for table number {table_number}. Table is now free.")
                reserved_table["order_total"] = 0
                reserved_table["reservation"] = None
            else:
                print("Invalid payment method.")
        else:
            print(f"Sorry, the table number {table_number} is not reserved.")
    else:
        print(f"Sorry, we do not have a table with number {table_number}.")


def check_admin_credentials(username, password):
        if username == "admin" and password == "1234":
            print("Logging into account, please wait...")
            time.sleep(1.5)
            print("Login to the system.")
            return True
        elif username == "restaurant" and password == "0000":
            print("Logging into account, please wait...")
            time.sleep(1.5)
            print("Login to the system.")
            return True
        elif username == "q" or username == "Q" or password == "Q" or password =="q":
            print("The system has been logged out.")
            quit()
        else:
            print("Wrong username or password...")
            return False
while True:

    print("Welcome to restaurant system. We wish you gave a good meal..")
    username = input("Please enter username :")
    password = input("Please enter password : ")
    if check_admin_credentials(username, password):
        while True:
            print("Please enter your choice. \n1-Make reservation \n2-Check Avaibility Reservation \n3-Order \n4-Select Payment Method\n5-EXIT")
            choice = int(input("----> "))
            if choice == 1:
                make_reservation()
            elif choice == 2:
                check_availability()
            elif choice == 3:
                table_number = int(input("Enter the number of the table you want to place order: "))
                make_order()
            elif choice == 4:
                pay_order()
            elif choice == 5:
                print("Exiting...")
                time.sleep(1.5)
                print("BYE BYE :)) ")
                break
            else:
                print("Invalid choice. Please try again.")

