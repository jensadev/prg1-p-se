import tkinter as tk
# Lista för att lagra saker i påsen
bag = ["kompass", "ficklampa", "första hjälpen kit"]

# Skapa huvudfönstret
window = tk.Tk()
window.title("Påsen 🎒")
window.geometry("500x500")

greeting = tk.Label(window, text="Välkommen till påsen 🎒")
greeting.pack(pady=10)

# Text area för att visa innehållet i påsen
text_area = tk.Text(window, height=15, width=50)
text_area.pack(pady=10)

# Visa innehållet i påsen
def show_bag_contents():
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, "I påsen hittar du:\n")
    for thing in bag:
        text_area.insert(tk.END, f"- {thing}\n")

def add_to_bag():
    item = entry.get()
    if item:
        bag.append(item)
        entry.delete(0, tk.END)

# Inmatningsfält för att lägga till saker i påsen
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Spara knapp
save_button = tk.Button(window, text="Spara i påsen [S]", command=add_to_bag)
save_button.pack(pady=10)

# Visa knapp
show_button = tk.Button(window, text="Visa innehållet i påsen [V]", command=show_bag_contents)
show_button.pack(pady=10)

# Avsluta knapp
exit_button = tk.Button(window, text="Avsluta programmet [Q]", command=window.quit)
exit_button.pack(pady=20)

# Kör programmet
window.mainloop()
