import tkinter as tk
import time

# Initialize global variables
button_pressed = False          # Tracks if the button is pressed
button_pressed_time = None      # Records the time when the button was pressed


def toggle_button():
    global button_pressed, button_pressed_time
    button_pressed = not button_pressed  # Toggle the state
    update_button_appearance()
    print(f"Button is now {'pressed' if button_pressed else 'unpressed'}.")

    if button_pressed:
        button_pressed_time = time.time()  # Record the time when the button was pressed
    else:
        button_pressed_time = None         # Reset the time

def update_button_appearance():
    if button_pressed:
        button.config(relief="sunken", text="Pressed", bg="lightblue")
    else:
        button.config(relief="raised", text="Unpressed", bg="SystemButtonFace")

def unpress_button():
    global button_pressed, button_pressed_time
    button_pressed = False
    button_pressed_time = None
    update_button_appearance()
    print("Button has been unpressed by the program.")

def main_program():
    # Simulate main program tasks
    print("Main program is running.")

    # Unpress the button after 5 seconds if it's pressed
    if button_pressed and button_pressed_time:
        elapsed_time = time.time() - button_pressed_time
        if elapsed_time >= 5:
            print("Program is unpressing the button after 5 seconds.")
            unpress_button()
    

    # Schedule the next call to main_program after 1000 milliseconds
    root.after(1000, main_program)

# Create the main window
root = tk.Tk()
root.title("Toggle Button Example")
root.geometry("300x200")

# Create the toggle button
button = tk.Button(root, text="Unpressed", width=15, command=toggle_button)
button.pack(pady=20)

# Start the main program loop
root.after(1000, main_program)

# Start the Tkinter event loop
root.mainloop()
