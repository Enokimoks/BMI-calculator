import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height / 100) ** 2
        if bmi < 18.5:
            status = "Underweight 😔"
        elif 18.5 <= bmi < 25:
            status = "Normal 😊"
        elif 25 <= bmi < 30:
            status = "Overweight 😐"
        else:
            status = "Obese 😟"
        result_label.config(text=f"BMI: {bmi:.2f}\nStatus: {status}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("Baymax BMI Calculator")
root.geometry("300x300")
root.config(bg="#ecf0f1")

tk.Label(root, text="Baymax BMI Calculator 🤖", font="lucida 15 bold", bg="#ecf0f1").pack(pady=10)

tk.Label(root, text="Enter Height (cm):", bg="#ecf0f1").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

tk.Label(root, text="Enter Weight (kg):", bg="#ecf0f1").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Button(root, text="Calculate", font="lucida 12 bold", bg="#74b9ff", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", bg="#ecf0f1", font="lucida 12")
result_label.pack(pady=10)

root.mainloop()
