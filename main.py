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
moving=0
margin=0.05
waiting=0
wait_threshold=5
previous_pos=Elevator_pos
prev_direction=Current_direction

def check_inbetween():
    if Current_target>Elevator_pos:
        target=np.ceil(Elevator_pos)
        for elem in Requests[np.ceil(Floor_index(Elevator_pos)):Floor_index(Current_target)]:
            if elem!=0:
                return target
            else:
                target+=1
        return Current_target
    else:
        target=np.floor(Elevator_pos)
        for elem in np.flip(Requests[Floor_index(Current_target):np.floor(Floor_index(Elevator_pos))]):
            if elem!=0:
                return target
            else:
                target-=1
        return Current_target
    
def check_all_down():
    global inside_objective
    target=lowest_floor
    for elem in Requests:
        if elem==2:
            inside_objective=target
            return target
        else:
            target+=1
    target=lowest_floor
    for elem in Requests:
        if elem!=0:
            return target
        else:
            target+=1
    return Elevator_pos
    
def check_all_up():
    global inside_objective
    target=Numb_floors+lowest_floor
    for elem in np.flip(Requests):
        if elem==2:
            inside_objective=target
            return target
        else:
            target+=1
    target=Numb_floors+lowest_floor
    for elem in np.flip(Requests):
        if elem!=0:
            return target
        else:
            target+=1
        return Elevator_pos
    
def check_over():
    if Current_target>Elevator_pos:
        target=Numb_floors+lowest_floor
        for elem in np.flip(Requests[np.ceil(Floor_index(Current_target)):]):
            if elem!=0:
                return target
            else:
                target-=1
        return Current_target
    else:
        target=lowest_floor
        for elem in Requests[:np.floor(Floor_index(Current_target))]:
            if elem!=0:
                return target
            else:
                target+=1
        return Current_target
            

def calculate_objective():
    global Current_target
    if moving==0:
        if prev_direction==-1: 
            Current_target=check_all_down
        else:
            Current_target=check_all_up
    if inside_objective!="none":
        return check_inbetween()
    else:
        return check_over

def calculate_direction():
    global moving
    global inside_objective
    global prev_direction
    if abs(Current_target-Elevator_pos)<margin or waiting<wait_threshold/dt:
        if previous_pos!=round(Elevator_pos):
            waiting=0  
            previous_pos=round(Elevator_pos)
        if Requests[Floor_index(Elevator_pos)]==2:
            inside_objective="none"
        Requests[Floor_index(Elevator_pos)]=0
        waiting+=1
        
        moving=0

        return 0
    elif Current_target>Elevator_pos:
        prev_direction=1
        return 1
    else:
        prev_direction=-1
        return -1
    


i=0

dt=0.01

max_time=20
while(i<max_time/dt):

    if i==300:
        Requests[2]=1
    if i==500:
        Requests[4]=1
    if i==502:
        Requests[1]=2
    if i==504:
        Requests[5]=1
    Current_target=calculate_objective()
    Current_direction=calculate_direction()
    Elevator_pos+=Current_direction*Max_speed*dt

    print(Elevator_pos)

    i+=1
    time.sleep(dt)

 
