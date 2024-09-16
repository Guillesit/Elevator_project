import numpy as np
import time
import math

Numb_floors=6
Elevator_pos=0
Current_target=0
Current_direction=0 #0 stop, 1 up, -1 down
Max_speed=0.3
Requests=np.zeros(Numb_floors)

lowest_floor=0
def Floor_index(Floor_num):
    
    return Floor_num-lowest_floor
def index_to_floor(index):
    return index+lowest_floor

inside_objective="none"
level_of_prio=0
margin=0.05
waiting=0
wait_threshold=5

def check_inbetween():
    if Current_target>Elevator_pos:
        target=np.ceil(Elevator_pos)
        for elem in Requests[np.ceil(Floor_index(Elevator_pos)):Floor_index(Current_target)]:
            if elem!=0:
                return target
            else:
                target+=1
    return Elevator_pos
            

def calculate_objective():
    if inside_objective!="none":
        return check_inbetween()
    elif

    return 

def calculate_direction():
    if abs(Current_target-Elevator_pos)<margin or waiting>wait_threshold/dt:
        Requests[Floor_index(Elevator_pos)]=0
        waiting+=1

        return 0
    elif Current_target>Elevator_pos:
        waiting=0
        return 1
    else:
        waiting=0
        return -1
    


i=0

dt=0.01

max_time=100
while(i<max_time/dt):

    Current_target=calculate_objective()
    Current_direction=calculate_direction()
    Elevator_pos+=Current_direction*Max_speed*dt



    i+=1
    time.sleep(dt)

 
