menu = {
    'Veg Pizza' : 250,
    'Chicken pizza' : 370,
    'Chicken Burger' : 170,
    'French Fries' : 110,
    'Iced Americano' : 120,
    'Hot Coffee' : 70,
    'Masala Tea' : 90,
    'Cold Drinks' : 85,
    'Ice-cream (chocolate/vanilla)' : 115,
    'Water' : 30,
    
    
}
print("welcome to your cafe . We are glad to serve you")
print("Veg Pizza : 250\nChicken pizza : 370\nChicken Burger : 170\nFrench Fries : 110\nIced Americano : 120\nHot Coffee : 70\nMasala Tea : 90\nCold Drinks : 85\nIce-cream (chocolate/vanilla) : 115\nWater : 30")
order_total = 0;
item_1 = input("Enter the item you want to order :")
if item_1 in menu:
   order_total += menu[item_1]
   print(f"dish {item_1} has been started preparing")
 
else:
    print(f"{item_1} is not in the menu")

second_order = input("Anything else you wanna have. Please enter yes or no :")

if second_order == "yes":
    item_2 = input("Enter the item you want to order :")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"dish {item_2} has been started preparing")
 
    else:
         print(f"{item_2} is not in the menu")
         
         
         
print(f"The total amount is {order_total}")