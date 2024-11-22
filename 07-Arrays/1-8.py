computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
k=0
b=1
computer_games = sorted(computer_games)
while k < len(computer_games):
    print(f"{b}.{computer_games[k]}")
    k = k + 1
    b = b + 1