resources= {
    "Water": 500,
    "Milk": 200,
    "Coffee": 100
}

Menu = {
    "latte": {
        "ingredients":{
                "Water": 200,
                "Milk": 150,
                "Coffee": 24,
        },
        "cost":150,
    },

    "espresso": {
        "ingredients":{
                "Water": 50,
                "Coffee": 18,
        },
        "cost":100,
    },

    "cappuccino": {
        "ingredients":{
                "Water": 250,
                "Milk": 100,
                "Coffee": 24,
        },
        "cost":200,
    },
}

def check_resources(order_ingredients):  #suppose customer wants latto
    for item in order_ingredients: #1st iteration ma item =water, 2nd iter ma item = milk, 3rd ma item = water 
                                    #yesma item() kina nagereko vanda item() le ky pani value pani dinxa but we just need value only. 
        if order_ingredients[item] > resources[item]: # 1st iteration ma latto ko water 200> resources ko water 500, .....
            print(f"Sorry there is not enough {item}")
            return False
        
            # print(f"There is enough {item}")
    print("There is enough resources to make coffee.")
    return True

def process_coins():
    print("please insert coins.")
    total = 0
    coins_five= int(input("How many 5rs coin?: "))
    coins_ten= int(input("How many 10rs coin?: "))
    coins_twenty= int(input("How many 20rs coin?: "))
    total = coins_five*5 + coins_ten*10 + coins_twenty*20
    return total

def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        profit = 0
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"here is your Rs.{money_received} - Rs.{coffee_cost} = Rs.{change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name}...Enjoy your day.")


asking= True
while asking:
    choice = input("What would you like to have? (Latte/ Espresso/ Cappuccino): ").strip().lower()
    
    if choice not in ["latte", "espresso", "cappuccino"]:
        print("We only have (Latte, Espresso, Cappuccino)")
        asking = input("Do you want any? ('yes/no'): ").strip().lower()
        if asking == "yes":
            continue
        elif asking == "no":
            print("Thanks for visiting.")
            asking = False

    else:# if choice == "latte" or "espresso" or "cappuccino":
        coffee_type = (Menu[choice])
        print(coffee_type)

        report_asking = input("Do you want to see current resources available in coffee machine? ('yes/no') :")
        if report_asking == "yes":
            for key, value in resources.items():
                print(f"{key}: {value}ml")

        if report_asking == 'yes' or 'no':
            #comparing resources    
           if check_resources(coffee_type["ingredients"]):               
            #    enough resources vaisakepaxi

            # entering coins from customer
               payment = process_coins() #total ko value payment ma aauxa
               print(f"You entered Rs.{payment} ")

            # checking payment
               if is_payment_successful(payment, coffee_type["cost"]):
                   make_coffee(choice, coffee_type["ingredients"])





        
    

    
    
    
        
    
