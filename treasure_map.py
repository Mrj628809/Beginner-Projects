# TREASURE_MAP
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x = position[0]
y = position[1]
map[int(x)-1][int(y)-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
