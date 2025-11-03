import random
import tkinter as tk
from tkinter import messagebox

# 🌺 List of flowers
flowers = [
    "🌸 Cherry Blossom", "🌼 Daisy", "🌻 Sunflower", "🌹 Rose", "🌷 Tulip", "💐 Lotus",
    "🌺 Hibiscus", "🌻 Marigold", "🌹 Jasmine", "🌼 Daffodil", "🌸 Peony", "🌺 Orchid",
    "🌷 Lily", "🌼 Camellia", "🌻 Dahlia", "🌸 Poppy", "🌺 Violet", "🌷 Iris", "🌼 Magnolia",
    "🌹 Carnation", "💐 Lavender", "🌸 Geranium", "🌺 Zinnia", "🌻 Petunia", "🌷 Azalea",
    "🌼 Chrysanthemum", "🌸 Bluebell", "🌺 Hydrangea", "🌹 Gardenia"
]

# 🌈 Color palette for flower names
colors = ["#e60026", "#ff66b2", "#ff8c00", "#006400", "#32cd32", "#ff1493", "#ff0000", "#ffd700"]

# 🌷 Function to generate flower
def get_flower():
    name = name_entry.get().strip()
    if name == "":
        messagebox.showwarning("Oops!", "Please enter your name first!")
        return
    flower = random.choice(flowers)
    color = random.choice(colors)
    result_label.config(
        text=f"Hello {name}!\n🌸 Your flower is 🌸",
        fg="#006400"  # dark green for message
    )
    flower_label.config(
        text=f"{flower}",
        fg=color
    )

# 🌼 Create main window
root = tk.Tk()
root.title("🌼 Name to Flower Generator 🌼")
root.geometry("520x420")
root.config(bg="#fffacd")  # light yellow background

# 🌸 Title label
heading = tk.Label(
    root,
    text="🌷 Name to Flower Generator 🌷",
    font=("Comic Sans MS", 18, "bold"),
    bg="#fffacd",
    fg="#d10000"  # bright red title
)
heading.pack(pady=15)

# 🌼 Name label
name_label = tk.Label(root, text="Enter your name:", font=("Arial", 12, "bold"), bg="#fffacd", fg="#006400")
name_label.pack()

# ✨ Name entry
name_entry = tk.Entry(root, font=("Arial", 12), justify="center", bg="#f5fffa", relief="solid", bd=2)
name_entry.pack(pady=8)

# 🌺 Button
generate_button = tk.Button(
    root,
    text="🌺 Get My Flower 🌺",
    font=("Arial", 12, "bold"),
    bg="#ff6347",  # tomato red
    fg="#fff",
    activebackground="#32cd32",  # bright green when clicked
    activeforeground="#fff",
    relief="raised",
    bd=3,
    command=get_flower
)
generate_button.pack(pady=10)

# 💖 Greeting message
result_label = tk.Label(
    root,
    text="",
    font=("Comic Sans MS", 13, "italic"),
    bg="#fffacd",
    fg="#006400"
)
result_label.pack(pady=10)

# 🌸 Decorative flower name
flower_label = tk.Label(
    root,
    text="",
    font=("Lucida Handwriting", 22, "bold"),
    bg="#fffacd"
)
flower_label.pack(pady=15)

# 🌼 Footer
footer=tk.Label(root, text="Let your name bloom into a flower",bg="#fffacd",fg="#b22222",font=("Arial",10,"italic"))
footer.pack(side="bottom", pady=8)

# 🌷 Run window
root.mainloop()