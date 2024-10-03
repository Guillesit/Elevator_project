import tkinter as tk
from PIL import Image, ImageTk
import threading
import queue
import time
import random  # For simulating backend data

# Initialize the main window
root = tk.Tk()
root.title("Data-Driven Animated Image")

# Set the window size
window_width = 400
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Create a Canvas widget
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Load images using PIL
try:
    image1_pil = Image.open("image1.png")
    image2_pil = Image.open("image2.png")
except FileNotFoundError:
    # If images are not found, create simple colored rectangles as placeholders
    image1_pil = Image.new("RGBA", (100, 100), (255, 0, 0, 255))  # Red square
    image2_pil = Image.new("RGBA", (100, 100), (0, 0, 255, 255))  # Blue square

# Optionally, resize images to fit the canvas
image_size = (100, 100)  # Width, Height
image1_pil = image1_pil.resize(image_size, Image.ANTIALIAS)
image2_pil = image2_pil.resize(image_size, Image.ANTIALIAS)

# Convert PIL images to ImageTk format
image1 = ImageTk.PhotoImage(image1_pil)
image2 = ImageTk.PhotoImage(image2_pil)

# Keep a reference to the images to prevent garbage collection
root.image1 = image1
root.image2 = image2

# Initial position of the image (center of the canvas)
x_pos = window_width // 2
y_pos = window_height // 2

# Add the image to the canvas
current_image = canvas.create_image(x_pos, y_pos, image=image1)

# Create a thread-safe queue for communication between backend and GUI
data_queue = queue.Queue()

def backend_data_producer(q):
    """
    Simulates backend data generation.
    In a real application, replace this with actual data retrieval or processing.
    """
    while True:
        # Simulate data arrival every 1 second
        time.sleep(1)

        # Simulate data: movement in y-axis (-1 for up, 1 for down, 0 for no movement)
        movement = random.choice([-1, 0, 1])

        # Simulate image toggle: True to switch to image1, False to image2
        toggle_image = random.choice([True, False])

        # Put the data into the queue
        q.put({'movement': movement, 'toggle_image': toggle_image})

# Create and start the backend thread
backend_thread = threading.Thread(target=backend_data_producer, args=(data_queue,), daemon=True)
backend_thread.start()

def update_gui():
    """
    Checks the data queue for new data and updates the image's position and appearance.
    """
    try:
        while not data_queue.empty():
            data = data_queue.get_nowait()
            movement = data.get('movement', 0)
            toggle_image_flag = data.get('toggle_image', False)

            # Update image position based on movement
            # movement: -1 (up), 0 (no movement), 1 (down)
            move_distance = 10  # Pixels to move per data step
            if movement == -1:
                canvas.move(current_image, 0, -move_distance)
            elif movement == 1:
                canvas.move(current_image, 0, move_distance)
            # movement == 0: no movement

            # Ensure the image stays within the canvas bounds
            coords = canvas.coords(current_image)
            new_y = coords[1]

            # Boundary checks
            if new_y < image_size[1] // 2:
                new_y = image_size[1] // 2
                canvas.coords(current_image, coords[0], new_y)
            elif new_y > window_height - image_size[1] // 
