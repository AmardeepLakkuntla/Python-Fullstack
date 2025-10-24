import os
import time

rooms=6
requests=int(input("enter the item"))#[3,4]
current_room=0

def draw_belt(requests):
    # print("🛤 convenyer belt is moving: ")
    for room in range(rooms):
        if room == requests:
            print("f   |📦|")
        else:
            print("f |  |")
            
            
print("items are moving in conveyner belt: ")
    
    
# for request in requests:
print("sorting the rooms{requests}:")
time.sleep(3)
draw_belt(requests)