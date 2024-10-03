import numpy as np
import time
import tkinter as tk
import time


#Index for Request, row for buttons, floor for everything else

root = tk.Tk()
root.title("Elevator")


Numb_floors=7
Elevator_pos=0
Current_target=0
Current_direction=0 #0 stop, 1 up, -1 down
Max_speed=1.2
lowest_floor=0
Top_floor=Numb_floors-lowest_floor-1
Requests=np.zeros((Numb_floors,3))


def floor_to_index(Floor_num):
    
    return int(round(Floor_num-lowest_floor))
def index_to_floor(index):
    return int(index+lowest_floor)

def row_to_floor(row_num):
    return Top_floor-row_num

def floor_to_row(floor_num):
    return Top_floor-floor_num

def row_to_index(row_num):
    return floor_to_index(row_to_floor(row_num))
def index_to_row(index):
    return floor_to_row(index_to_floor(index))




inside_objective="none"
moving=0
margin=0.05
waiting=0.0
open_doors_toggle=[0]
wait_threshold=1



attempted_direction=1
next_direction=0


def toggle_button(row,column):
    global Requests
    Requests[row_to_index(row),column] = int(not Requests[row_to_index(row),column])  # Toggle the state
    update_button_appearance(row,column)
    #print(f"Button is now {'pressed' if button_pressed else 'unpressed'}.")
    '''
    if button_pressed:
        button_pressed_time = time.time()  # Record the time when the button was pressed
    else:
        button_pressed_time = None         # Reset the time
    '''

def update_button_appearance(row,column):
    global buttons
    
    if Requests[row_to_index(row),column]:
        buttons[row][column].config(relief="sunken", bg="lightblue")
    else:
        buttons[row][column].config(relief="raised", bg="SystemButtonFace")

def unpress_button(row,column):
    global Requests
    global buttons
    #global button_pressed, button_pressed_time
    Requests[row_to_index(row),column]=0
    update_button_appearance(row,column)
    print("Button has been unpressed by the program.")

def toggle_button_alt(togglable,button):
    
    togglable[0] = int(not togglable[0])  # Toggle the state
    update_button_appearance_alt(togglable,button)
    #print(f"Button is now {'pressed' if button_pressed else 'unpressed'}.")
    '''
    if button_pressed:
        button_pressed_time = time.time()  # Record the time when the button was pressed
    else:
        button_pressed_time = None         # Reset the time
    '''

def update_button_appearance_alt(togglable,button):
    if togglable[0]:
        button.config(relief="sunken", bg="lightblue")
    else:
        button.config(relief="raised", bg="SystemButtonFace")

def unpress_button_alt(togglable,button):
    #global button_pressed, button_pressed_time
    togglable[0]=0
    update_button_appearance_alt(togglable,button)
    print("Button has been unpressed by the program.")

# Initialize an empty list to store the buttons
buttons = []#np.zeros(7*3)

# Create 7 rows and 3 columns of buttons
for row in range(Numb_floors):
    row_buttons = []  # List to store buttons in the current row
    for col in range(3):
        match col:
            case 0:
                symbol="↓"
            case 1:
                symbol="↑"
            case _:
                symbol="Ø"
                


        btn = tk.Button(root, text=f'{Top_floor-row}º '+symbol, width=10)
        btn.grid(row=row, column=col, padx=5, pady=5)
        
        row_buttons.append(btn)  # Add the button to the row list
    buttons.append(row_buttons)  # Add the row list to the main buttons list

for row2 in range(Numb_floors):
    for col2 in range(3):
        buttons[row2][col2].config(command=lambda colu=col2, rows=row2: toggle_button(rows,colu))
        pass

def do_nothing():
    pass

# Create an extra button below the grid, spanning all three columns
extra_button = tk.Button(root, text='Hold the door', width=32, relief=tk.RAISED)
extra_button.config(command=lambda: toggle_button_alt(open_doors_toggle,extra_button))
extra_button.grid(row=Numb_floors, column=0, columnspan=3, padx=5, pady=10)


def calculate_objective():
    global next_direction 
    global Current_target
    
    if (attempted_direction==1 and Current_direction==0):
        target=int(round(Elevator_pos))+1 #1! y 3
        for elem in Requests[floor_to_index((round(Elevator_pos))+1):,2]:
            if elem!=0:
                target=int(round(Elevator_pos))+1
                for elem in Requests[floor_to_index((round(Elevator_pos))+1):,2]+Requests[floor_to_index((round(Elevator_pos))+1):,1]:
                    if elem!=0:
                        return target
                else:
                    target+=1
            else:
                target+=1

        target=int(round(Elevator_pos))-1 #2! y 6
        for elem in np.flip(Requests[:floor_to_index(round((Elevator_pos))-1)+1,2]):
            if elem!=0:
                
                target=int(round(Elevator_pos))-1
                for elem in np.flip(Requests[:floor_to_index((round(Elevator_pos))-1)+1,2]+Requests[:floor_to_index((round(Elevator_pos))-1)+1,0]):
                    if elem!=0:
                        
                        return target
                else:
                    target-=1
            else:
                target-=1

        target=int(round(Elevator_pos))+1 #3
        for elem in Requests[floor_to_index((round(Elevator_pos))+1):,1]:
            if elem!=0:
                next_direction=1
                return target
            else:
                target+=1



        target=Top_floor #5 y 6
        for elem in np.flip(Requests[:,0]):
            if elem!=0:
                next_direction=-1
                
                return target
            else:
                target-=1


        
        target=lowest_floor # 4
        for elem in Requests[:floor_to_index((round(Elevator_pos))-1)+1,1]:
            if elem!=0:
                next_direction=1
                return target
            else:
                target+=1
            
        return Current_target
    
    elif Current_direction==0:

        target=int(round(Elevator_pos))-1 #2! y 6
        for elem in np.flip(Requests[:floor_to_index((round(Elevator_pos))-1)+1,2]):
            if elem!=0:
                target=int(round(Elevator_pos))-1
                for elem in np.flip(Requests[:floor_to_index((round(Elevator_pos))-1)+1,2]+Requests[:floor_to_index((round(Elevator_pos))-1)+1,0]):
                    if elem!=0:
                        
                        return target
                else:
                    target-=1
            else:
                target-=1

        target=int(round(Elevator_pos))+1 #1! y 3
        for elem in Requests[floor_to_index((round(Elevator_pos))+1):,2]:
            if elem!=0:
                target=int(round(Elevator_pos))+1
                for elem in Requests[floor_to_index((round(Elevator_pos))+1):,2]+Requests[floor_to_index((round(Elevator_pos))+1):,1]:
                    if elem!=0:
                        
                        return target
                else:
                    target+=1
            else:
                target+=1
        
        target=(round(Elevator_pos))-1 # 6
        for elem in np.flip(Requests[:floor_to_index((round(Elevator_pos))-1)+1,0]):
            if elem!=0:
                next_direction=-1
                
                return target
            else:
                target-=1
        
        target=lowest_floor #3 y 4
        for elem in Requests[:,1]:
            if elem!=0:
                next_direction=1
                
                return target
            else:
                target+=1


        target=Top_floor #5
        for elem in np.flip(Requests[floor_to_index((round(Elevator_pos))+1):,0]):
            if elem!=0:
                next_direction=-1
                
                
                return target
            else:
                target-=1
        
        return Current_target
    
    elif Current_direction==1:

        target=int(np.ceil(Elevator_pos)) #1 y 3
        for elem in Requests[floor_to_index((np.ceil(Elevator_pos))):,2]+Requests[floor_to_index((np.ceil(Elevator_pos))):,1]:
            if elem!=0:
                
                return target     
            else:
                target+=1

        
        target=Top_floor #5
        for elem in np.flip(Requests[floor_to_index(np.ceil(Elevator_pos)):,0]):
            if elem!=0:
                next_direction=-1
                return target
            else:
                target-=1

        target=int(np.floor(Elevator_pos)) #2 y 6
        for elem in np.flip(Requests[:floor_to_index(np.floor(Elevator_pos))+1,2]+Requests[:floor_to_index(np.floor(Elevator_pos))+1,0]):
            if elem!=0:
                
                return target
            else:
                target-=1

        target=lowest_floor # 4
        for elem in Requests[:floor_to_index((np.floor(Elevator_pos)))+1,1]:
            if elem!=0:
                next_direction=1
                return target
            else:
                target+=1

        return Current_target
    else:
        target=int(np.floor(Elevator_pos)) #2 y 6
        for elem in np.flip(Requests[:floor_to_index(np.floor(Elevator_pos))+1,2]+Requests[:floor_to_index(np.floor(Elevator_pos))+1,0]):
            if elem!=0:
                
                return target
            else:
                target-=1

        target=lowest_floor # 4
        for elem in Requests[:floor_to_index((np.floor(Elevator_pos)))+1,1]:
            if elem!=0:
                next_direction=1
                return target
            else:
                target+=1

        target=int(np.ceil(Elevator_pos)) #1 y 3
        for elem in Requests[floor_to_index((np.ceil(Elevator_pos))):,2]+Requests[floor_to_index((np.ceil(Elevator_pos))):,1]:
            if elem!=0:
                
                return target     
            else:
                target+=1

        target=Top_floor #5
        for elem in np.flip(Requests[floor_to_index((np.ceil(Elevator_pos))):,0]):
            if elem!=0:
                next_direction=-1
                return target
            else:
                target-=1
    
        return Current_target




def calculate_direction():
    global moving
    global inside_objective
    global attempted_direction
    global next_direction
    global open_doors_toggle
    global waiting


    if abs(Current_target-Elevator_pos)<margin:
        if next_direction==1:
            Requests[floor_to_index(round(Elevator_pos)),1]=0
            update_button_appearance(floor_to_row(round(Elevator_pos)),1)
            next_direction=0
        if next_direction==-1:
            Requests[floor_to_index(round(Elevator_pos)),0]=0
            update_button_appearance(floor_to_row(round(Elevator_pos)),0)
            next_direction==0
        


    if abs(Current_target-Elevator_pos)>=margin:
        if Current_target>Elevator_pos:
            attempted_direction=1
            #Requests[floor_to_index(round(Elevator_pos)),1]=0
            #update_button_appearance(floor_to_row(round(Elevator_pos)),1)

        else:
            attempted_direction=-1
            #Requests[floor_to_index(round(Elevator_pos)),0]=0
            #update_button_appearance(floor_to_row(round(Elevator_pos)),0)

        

    if abs(Current_target-Elevator_pos)<margin or waiting>0:
        
        if moving:
            moving=0
            waiting=wait_threshold/dt
        
        if open_doors_toggle[0]:
            open_doors_toggle[0]=0
            unpress_button_alt(open_doors_toggle,extra_button)
            if not moving:
                waiting=wait_threshold/dt

        Requests[floor_to_index(round(Elevator_pos)),2]=0
        update_button_appearance(floor_to_row(round(Elevator_pos)),2)

        if waiting>0:
            waiting-=1
        
        #moving=0

        return 0
    else:
        moving=1
        return attempted_direction
    


i=0

dt=0.02

max_time=5

def main_program():
    global Current_direction, Current_target, Elevator_pos,i
    Current_target=calculate_objective()
    
    Current_direction=calculate_direction()
    #print("Attempted_dir:",attempted_direction,"Curr_direction:",Current_direction,"waiting_time:",waiting)
    
    Elevator_pos+=Current_direction*Max_speed*dt
    print("i:",i," Curr_target:",Current_target,"Elevator_pos:","{:.3f}".format(Elevator_pos),"Waiting_time:",waiting)
    
    i+=1
    root.after(int(dt*1000),main_program)
    return

root.after(int(dt*1000),main_program)

root.mainloop()

'''
    if i==5:
        Requests[2,0]=1
    
    if i==202:
        Requests[1,2]=1
    
    if i==400:
        Requests[4,0]=1
    if i==404:
        Requests[5,0]=1
'''



print(Requests)
