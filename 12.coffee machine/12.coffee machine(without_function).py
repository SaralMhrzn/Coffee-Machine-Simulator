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
            order_coffee = coffee_type["ingredients"]
            # checking sufficient resources
            for item in order_coffee(): #compares each item ko value 
                                        #yesma item() kina nagereko vanda item() le ky pani value pani dinxa but we just need value only.
                if order_coffee[item] > resources[item]:
                    print(f"there is no sufficient {item}")
                    print("Your ordered coffee is cancelled")
                    exit()
                
                else:
                    print(f"There is sufficient {item}")

            
            print("please insert coins.")
            total = 0
            coins_five= int(input("How many 5rs coin?: "))
            coins_ten= int(input("How many 10rs coin?: "))
            coins_twenty= int(input("How many 20rs coin?: "))
            total = coins_five*5 + coins_ten*10 + coins_twenty*20
            print(f"you entered Rs.{total}")

        # checking payment
        if total <= coffee_type["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            
        else:
            profit = 0
            profit += coffee_type["cost"]
            change = total - coffee_type["cost"]
            print(f"here is your Rs.{total} - Rs.{coffee_type["cost"]} = Rs.{change} in change.")

            for item in order_coffee:
                resources[item] -= order_coffee[item]
            print(f"Here is your {choice}...Enjoy your day.")
                

            
                



                     
                    
           




        
    

    
    
    
        
    
