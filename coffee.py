menu={"espresso":
      {"ingredients":
       {"water":50,"milk":0,"coffee":20},
       "price":1.5},
       
      "latte":{"ingredients":
        {"water":60,"milk":100,"coffee":25},
        "price":2.5},
        
        "cappuccino":
        {"ingredients":
        {"water":100,"milk":80,"coffee":25},
        "price":2}}

materials={"milk":2000,"water":3000,"coffee":1000,"money":0}
end=False

while end!=True:
    order=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order=="off":
        end=True
    elif order=="report":
        print(f"Water: {materials['water']}ml")
        print(f"Milk: {materials['milk']}ml")
        print(f"Coffee: {materials['coffee']}g")
        print(f"Money: ${materials['money']}")
    elif materials['water']>=menu[order]['ingredients']['water']:
        if materials['milk']>=menu[order]['ingredients']['milk']:
            if materials['coffee']>=menu[order]['ingredients']['coffee']:
                print("Please insert coins.")
                dollar=int(input("How many dollars: "))
                quarters=int(input("How many quarters?: "))
                dimes=int(input("How many dimes?: "))
                
                total=quarters*0.25+dimes*0.1+dollar*1
                if total>=menu[order]['price']:
                    change=round(total-menu[order]['price'],2)
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {order}. Enjoy!")
                    materials['money']+=menu[order]['price']
                    materials['water']-=menu[order]['ingredients']['water']
                    materials['milk']-=menu[order]['ingredients']['milk']
                    materials['coffee']-=menu[order]['ingredients']['coffee']
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    
        
    
