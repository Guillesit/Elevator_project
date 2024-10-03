import tkinter as tk
from PIL import Image, ImageTk
import random

def update_image_position():
    # Simulate receiving data from the backend (e.g., sensor data)
    backend_value = random.randint(0, 400)  # Simulate backend data
    image_choice = random.choice([0, 1])    # Simulate a parameter to switch images (0 or 1)
    slider.update_idletasks()
    # Update the slider's value programmatically based on backend value
    slider.set(backend_value)

    # Move the image label based on the slider value
    y_position = slider.get()
    canvas.coords(image_label, 100, y_position)

    # Switch between two images based on the parameter
    if image_choice == 0:
        canvas.itemconfig(image_label, image=tk_image1)  # Show first image
    else:
        canvas.itemconfig(image_label, image=tk_image2)  # Show second image

    # Schedule the function to run again after 1000ms (1 second)
    root.after(1000, update_image_position)

# Create the main window
root = tk.Tk()
root.title("Image Switching Based on Backend Data")

# Create a canvas to display the image
canvas = tk.Canvas(root, width=200, height=400)
canvas.pack(side="left", padx=20, pady=20)

# Load two images using PIL (You can replace these with your actual image paths)
image1 = Image.open("open.webp")  # Use your first image path here
image2 = Image.open("closed.webp")  # Use your second image path here

# Resize the images to fit the canvas
image1 = image1.resize((50, 50))
image2 = image2.resize((50, 50))

# Convert the images to a format Tkinter can display
tk_image1 = ImageTk.PhotoImage(image1)
tk_image2 = ImageTk.PhotoImage(image2)

# Create a label on the canvas to display the image, initially showing the first image
image_label = canvas.create_image(100, 200, image=tk_image1)  # Initial position (x, y)

# Create a slider (Scale widget) to control the vertical movement, disabled to prevent user control
slider = tk.Scale(root, from_=400, to=0, orient="vertical")
slider.set(200)  # Set the initial value of the slider
slider.pack(side="right", padx=20, pady=20)
slider.config(state="disabled")  # Disable user interaction with the slider
slider.update_idletasks()

# Start the periodic updates based on backend data
root.after(1000, update_image_position)

# Start the Tkinter main loop
root.mainloop()
