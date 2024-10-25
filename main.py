import tkinter as tk

root = tk.Tk()
root.title("Vocal color detector")
root.geometry("600x500") 


def start_record():
    text_display.insert(tk.END, "Début\n")

title_label = tk.Label(root, text="Vocal color detector", font=("Arial", 24, "italic"))
title_label.pack(pady=20)
text_display = tk.Text(root, height=10, width=50, font=("Arial", 14))
text_display.pack(pady=20)
record_button = tk.Button(root, text="Start record", font=("Arial", 16), bg="orange", fg="white", command=start_record)
record_button.pack(pady=10)
footer_label = tk.Label(root, text="Footer", font=("Arial", 14))
footer_label.pack(side="bottom", pady=20)

root.mainloop()