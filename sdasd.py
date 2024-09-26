import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Button Grid")

# Initialize an empty list to store the buttons
buttons = []

# Create 7 rows and 3 columns of buttons
for row in range(7):
    row_buttons = []  # List to store buttons in the current row
    for col in range(3):
        btn = tk.Button(root, text=f'Button {row * 3 + col + 1}', width=10)
        btn.grid(row=row, column=col, padx=5, pady=5)
        row_buttons.append(btn)  # Add the button to the row list
    buttons.append(row_buttons)  # Add the row list to the main buttons list

# Create an extra button below the grid, spanning all three columns
extra_button = tk.Button(root, text='Extra Button', width=32)
extra_button.grid(row=7, column=0, columnspan=3, padx=5, pady=10)

# Run the application
root.mainloop()
