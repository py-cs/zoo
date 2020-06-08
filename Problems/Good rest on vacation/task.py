# put your python code here
duration = int(input())
food_per_day = int(input())
one_way_flight = int(input())
hotel_per_night = int(input())

print(food_per_day * duration + one_way_flight * 2 + hotel_per_night * (duration - 1))