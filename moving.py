import tkinter as tk
from PIL import Image, ImageTk

# Sample data for Y positions (you can replace this with your actual data)
y_positions = [50, 100, 150, 200, 250, 200, 150, 100, 50]
index = 0
elevator_open = True

def move_elevator():
    global index
    # Get the next Y position from the data
    y = y_positions[index]
    index = (index + 1) % len(y_positions)  # Loop through the list
    
    # Move the elevator to the new Y position
    canvas.coords(elevator_image_on_canvas, 100, y)  # x stays 100, y varies
    
    # Call the function again after a short delay (100 ms)
    window.after(100, move_elevator)

def toggle_door():
    global elevator_open
    if elevator_open:
        canvas.itemconfig(elevator_image_on_canvas, image=tk_elevator_closed)
    else:
        canvas.itemconfig(elevator_image_on_canvas, image=tk_elevator_open)
    elevator_open = not elevator_open

# Create the main window
window = tk.Tk()
window.title("Elevator Simulation")

# Create a canvas to display the background and elevator images
canvas = tk.Canvas(window, width=300, height=400)
canvas.pack()

# Load the background image (elevator shaft)
background_img = Image.open("109605.png")  # Update with the background image path
background_img = background_img.resize((300, 400))
tk_background = ImageTk.PhotoImage(background_img)
canvas.create_image(0, 0, anchor=tk.NW, image=tk_background)

# Load the two elevator images (open and closed)
elevator_open_img = Image.open("open.webp")  # Replace with open image path
elevator_open_img = elevator_open_img.resize((50, 100))  # Resize if needed
tk_elevator_open = ImageTk.PhotoImage(elevator_open_img)

elevator_closed_img = Image.open("closed.webp")  # Replace with closed image path
elevator_closed_img = elevator_closed_img.resize((50, 100))  # Resize if needed
tk_elevator_closed = ImageTk.PhotoImage(elevator_closed_img)

# Add the elevator (default to open) to the canvas
elevator_image_on_canvas = canvas.create_image(100, 50, anchor=tk.NW, image=tk_elevator_open)

# Create a button to toggle between open and closed doors
toggle_button = tk.Button(window, text="Toggle Door", command=toggle_door)
toggle_button.pack()

# Start moving the elevator
move_elevator()

# Start the Tkinter event loop
window.mainloop()

