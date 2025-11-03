import random

# 🌸 List of beautiful flowers
flowers = [
    "🌸 Cherry Blossom",
    "🌼 Daisy",
    "🌻 Sunflower",
    "🌹 Rose",
    "🌷 Tulip",
    "💐 Lotus",
    "🌺 Hibiscus",
    "🌻 Marigold",
    "🌹 Jasmine",
    "🌼 Daffodil",
    "🌸 Peony",
    "🌺 Orchid",
    "🌷 Lily",
    "🌼 Camellia",
    "🌻 Dahlia",
    "🌸 Poppy",
    "🌺 Violet",
    "🌷 Iris",
    "🌼 Magnolia",
    "🌹 Carnation",
    "💐 Lavender",
    "🌸 Geranium",
    "🌺 Zinnia",
    "🌻 Petunia",
    "🌷 Azalea",
    "🌼 Chrysanthemum",
    "🌸 Bluebell",
    "🌺 Hydrangea",
    "🌹 Gardenia"
]

# Ask user for their name
name = input("Enter your name: ")

# Randomly choose a flower
flower = random.choice(flowers)

# Display the result
print(f"Hello {name}! 🌸 Your flower is: {flower}")
