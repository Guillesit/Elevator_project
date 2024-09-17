import numpy as np
import time
import math

Numb_floors=6
Elevator_pos=0
Current_target=0
Current_direction=0 #0 stop, 1 up, -1 down
Max_speed=0.3
lowest_floor=0
Top_floor=Numb_floors-lowest_floor
Requests=np.zeros(Numb_floors-lowest_floor,3)


def Floor_index(Floor_num):
    
    return int(Floor_num-lowest_floor)
def index_to_floor(index):
    return int(index+lowest_floor)

inside_objective="none"
moving=0
margin=0.05
waiting=0
wait_threshold=5
previous_pos=Elevator_pos
print(previous_pos)
attempted_direction=1
next_direction=0

'''

def check_inbetween():
    if Current_target>Elevator_pos:
        target=np.ceil(Elevator_pos)
        for elem in Requests[Floor_index(np.ceil(Elevator_pos)):Floor_index(Current_target)]:
            if elem!=0:
                return target
            else:
                target+=1
        return Current_target
    else:
        target=np.floor(Elevator_pos)
        for elem in np.flip(Requests[Floor_index(Current_target):Floor_index(np.floor(Elevator_pos))]):
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
        for elem in np.flip(Requests[Floor_index(np.ceil(Current_target)):]):
            if elem!=0:
                return target
            else:
                target-=1
        return Current_target
    else:
        target=lowest_floor
        for elem in Requests[:Floor_index(np.floor(Current_target))]:
            if elem!=0:
                return target
            else:
                target+=1
        return Current_target
            
'''
def calculate_objective():
    global next_direction 
    
    if attempted_direction==1 and Current_direction==0:
        target=int(round(Elevator_pos))+1 #1! y 3
        for elem in Requests[Floor_index((round(Elevator_pos))+1):,2]:
            if elem!=0:
                target=int(round(Elevator_pos))+1
                for elem in Requests[Floor_index((round(Elevator_pos))+1):,2]+Requests[Floor_index((round(Elevator_pos))+1):,1]:
                    if elem!=0:
                        return target
                else:
                    target+=1
            else:
                target+=1

        target=int(round(Elevator_pos))-1 #2! y 6
        for elem in np.flip(Requests[:Floor_index(np.floor(Elevator_pos)),2]):
            if elem!=0:
                target=int(round(Elevator_pos))-1
                for elem in np.flip(Requests[:Floor_index((round(Elevator_pos))-1),2]+Requests[:Floor_index((round(Elevator_pos))-1),0]):
                    if elem!=0:
                        return target
                else:
                    target-=1
            else:
                target-=1

        target=int(round(Elevator_pos))+1 #3
        for elem in Requests[Floor_index((round(Elevator_pos))+1):,1]:
            if elem!=0:
                return target
            else:
                target+=1



        target=Top_floor #5 y 6
        for elem in np.flip(Requests[:,0]):
            if elem!=0:
                return target
            else:
                target-=1


        
        target=lowest_floor # 4
        for elem in Requests[:Floor_index((round(Elevator_pos))-1),1]:
            if elem!=0:
                return target
            else:
                target+=1
            
        return Current_target
    
    elif Current_direction==0:

        target=int(round(Elevator_pos))-1 #2! y 6
        for elem in np.flip(Requests[:Floor_index(np.floor(Elevator_pos)),2]):
            if elem!=0:
                target=int(round(Elevator_pos))-1
                for elem in np.flip(Requests[:Floor_index((round(Elevator_pos))-1),2]+Requests[:Floor_index((round(Elevator_pos))-1),0]):
                    if elem!=0:
                        return target
                else:
                    target-=1
            else:
                target-=1

        target=int(round(Elevator_pos))+1 #1! y 3
        for elem in Requests[Floor_index((round(Elevator_pos))+1):,2]:
            if elem!=0:
                target=int(round(Elevator_pos))+1
                for elem in Requests[Floor_index((round(Elevator_pos))+1):,2]+Requests[Floor_index((round(Elevator_pos))+1):,1]:
                    if elem!=0:
                        return target
                else:
                    target+=1
            else:
                target+=1
        
        target=(round(Elevator_pos))-1 # 6
        for elem in np.flip(Requests[:Floor_index((round(Elevator_pos))-1),1]):
            if elem!=0:
                return target
            else:
                target-=1
        
        target=Top_floor #3 y 4
        for elem in Requests[:,0]:
            if elem!=0:
                return target
            else:
                target+=1


        target=int(round(Elevator_pos))-1 #5
        for elem in np.flip(Requests[:Floor_index((round(Elevator_pos))+1),0]):
            if elem!=0:
                return target
            else:
                target-=1
    
    elif Current_direction==1:

        return Current_target





def calculate_direction():
    global moving
    global inside_objective
    global attempted_direction

    if abs(Current_target-Elevator_pos)<margin:

        pass


    if abs(Current_target-Elevator_pos)>=margin:
        if Current_target>Elevator_pos:
            attempted_direction=1
            Requests[Floor_index(Elevator_pos),1]=0

        else:
            attempted_direction=-1
            Requests[Floor_index(Elevator_pos),0]=0


    if abs(Current_target-Elevator_pos)<margin or waiting<wait_threshold/dt:
        
        if previous_pos!=round(Elevator_pos):
            waiting=0
            previous_pos=round(Elevator_pos)

        Requests[Floor_index(round(Elevator_pos)),2]=0
        waiting+=1
        
        #moving=0

        return 0
    else:
        
        return attempted_direction
    


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

    print("Elevator_pos:\n",Elevator_pos)

    i+=1
    time.sleep(dt)

 
