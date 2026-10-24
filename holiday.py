print("========================================")
print("welcome to your holiday planner")
print("========================================")

print("step 1 pick your holiday activity")
print("1 - country visit trip")
print("2 - car trip")

choice = int(input("enter 1 or 2: " ))
print()

if choice == 1:
    print("step 2 pick how will you visit")
    print("1 - flight")
    print("2 - overnight train")
print()

transport_type = int(input("enter 1 or 2: "))
print()
    
if transport_type == 1:
    print("You picked flight.")
elif transport_type == 2:
    print("You picked overnight train.")

if transport_type == 1:
    print("you picked    : flight")
    print("top speed     : 1000 km/h")
    print("best for      : long distance travel")
elif transport_type == 2:
    print("you picked    : overnight train")
    print("top speed     : 200 km/h")
    print("best for      : long distance travel")

if choice == 2:
    print("step 2 pick your car type")
    print("1 - sedan")
    print("2 - SUV")
    car_type = int(input("enter 1 or 2: "))
    print()

    if car_type == 1:
        print("you picked    : sedan")
        print("seats         : 5 passengers")
        print("best for      : family trips")
    elif car_type == 2:
        print("you picked    : SUV")
        print("seats         : 7 passengers")
        print("best for      : off road adventures")
    else:
        print("that was not a valid choice please enter 1 or 2 ")
     


