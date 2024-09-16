import numpy as np

Numb_floors=6
Elevator_pos=0
Current_target=0
Current_direction="up"
Max_speed=0
Requests=np.zeros(Numb_floors)

lowest_floor=0
def Floor_index(Floor_num):
    
 return Floor_num-lowest_floor

i=0
while(i<100):

 i+=1
 sleep(10)
 
