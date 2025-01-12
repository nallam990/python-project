import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Get user inputs
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        # Perform the selected operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        # Display the result
        label_result.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Choose operation:").grid(row=2, column=0, padx=10, pady=5)

# Create radio buttons for operation selection
operation_var = tk.StringVar(value="+")
tk.Radiobutton(root, text="Addition (+)", variable=operation_var, value="+").grid(row=3, column=0, padx=10, pady=2)
tk.Radiobutton(root, text="Subtraction (-)", variable=operation_var, value="-").grid(row=3, column=1, padx=10, pady=2)
tk.Radiobutton(root, text="Multiplication (*)", variable=operation_var, value="*").grid(row=4, column=0, padx=10, pady=2)
tk.Radiobutton(root, text="Division (/)", variable=operation_var, value="/").grid(row=4, column=1, padx=10, pady=2)

# Create a button to calculate
btn_calculate = tk.Button(root, text="Calculate", command=calculate)
btn_calculate.grid(row=5, column=0, columnspan=2, pady=10)

# Create a label to display the result
label_result = tk.Label(root, text="Result: ", font=("Arial", 12))
label_result.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
