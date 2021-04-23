#Joburg_Derimit_Task

driver_speed = float(input("Average speed on the road in km/h?: "))
road_speed = float(input("Allowed road speed in km/h?: "))

demerit_points = (driver_speed - road_speed)/5

if driver_speed <= 60:
    print("OK")
elif driver_speed > road_speed:
    print("Points: " + str(demerit_points))

    if demerit_points > 12:
        print("Time to go to jail!")
