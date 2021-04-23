#defining hotel_cost
def hotel_cost(nights):
    return 140*nights

#defining plane_ride_cost
def plane_ride_cost(city):
    if 'Cape Town' == "city":
        return 2500
    elif 'Durban' == "city":
        return 2300
    elif 'JHB' == "city":
        return 2000
    elif 'BFN' == "city":
        return 1800

#rental_car_cost
def rental_car_cost(days):
    car_cost = 40*7
    if days >=7:
        car_cost -= 50
    elif days >= 3:
        car_cost -= 20
        return car_cost


#trip_cost
def trip_cost(city, days, spending_money):
    (rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money)
    print(trip_cost("BFN, 2, 1000"))







