import tkinter as tk
from PIL import Image, ImageTk

# Sample data for Y positions (you can replace this with your actual data)
y_positions = [50, 100, 150, 200, 250, 200, 150, 100, 50]
index = 0

def move_image():
    global index
    # Get the next Y position from the data
    y = y_positions[index]
    index = (index + 1) % len(y_positions)  # Loop through the list
    
    # Move the image to the new Y position
    canvas.coords(image_on_canvas, 100, y)  # x stays 100, y varies
    
    # Call the function again after a short delay (100 ms)
    window.after(100, move_image)

# Create the main window
window = tk.Tk()
window.title("Moving Image Example")

# Create a canvas to display the image
canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

# Load an image using PIL
img = Image.open("open.webp")  # Replace with your image path
img = img.resize((50, 50))  # Resize the image if needed
tk_img = ImageTk.PhotoImage(img)

# Add the image to the canvas at a starting position
image_on_canvas = canvas.create_image(100, 50, anchor=tk.NW, image=tk_img)

# Start moving the image
move_image()

# Start the Tkinter event loop
window.mainloop()
