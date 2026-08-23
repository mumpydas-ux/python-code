tempreture = int(input("enter todays tempreture in celsius: "))

if tempreture < 20:
    outfit = "jacket"
    print("it is cold today")
    print("wear a", outfit)
else:
    outfit = "t-shirt"
    print("it is warm today")
    print("wear a", outfit) 

    is_raining = input("is it raining today? (yes/no): ")

    if is_raining == "yes":
        print("bring an umbrella")

        wind_speed = int(input("enter the wind speed in km/h: "))

        if wind_speed > 30:
            print("it is windy today")
            print("wear a windbreaker , wear a windbreaker over you")
        else:
            print("it is calm today")
            print("no need for a windbreaker over your , outfit")
            
          
 