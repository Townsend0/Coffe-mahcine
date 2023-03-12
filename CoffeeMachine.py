import os
g={"espresso": [50,0,18,1.5], "latte": [200,150,24,2.5], "cappuccino": [250,100,24,3] }
a=['Water','Milk','Coffee','Money']
b={ 'Water': 300, 'Milk': 200, 'Coffee': 100, 'Money': 0 }
def coin(e,g):
    c=True
    while c:
        d=0
        print("\nPlease insert coins.\n")
        d+=int(input("How many quarters?: "))*0.25
        d+=int(input("How many dimes?: "))*0.1
        d+=int(input("How many nickles?: "))*0.05
        d+=int(input("How many pennies?: "))*0.01
        if d<g[e][3]:
            os.system("clear")
            print(f"\nSorry that's not enough money, {e} is ${g[e][3]}, money refunded")
            return False
        else:
            if d>g[e][3]:
                print(f"\nHere is ${d-g[e][3]} your change")
            b[a[3]]+=g[e][3]
            return True

def check(e,g,a,b):
    c=True
    for f in range(3):
        if g[e][f]>b[a[f]]:
            c=False
            print(f"Sorry there is not enough {a[f]}.")
    return c        

def order(a,b,e,g):
    for f in range(3):
        b[a[f]]-=g[e][f]
    print(f"Here is your {e} ☕️. Enjoy!")
        
def rep(a,b):
    for c in range(2):
        print(f"{a[c]}: {b[a[c]]}ml")
    print(f"{a[2]}: {b[a[2]]}g\n{a[3]}: ${b[a[3]]}")

while True:
    e=input("\nWhat would you like? [ Espresso, Latte, Cappuccino ]: ").lower()
    if e=='report':
        os.system("clear")
        rep(a,b)
    elif e!='latte' and e!='espresso' and e!='cappuccino':
        os.system("clear")
        print("\n( Invalid input! )")
    elif e=='off':
        exit()
    else:
        os.system("clear")
        if check(e,g,a,b):
            if coin(e,g):
                order(a,b,e,g)