# colors = [11, 34, 98, 43, 45, 54, 54]
# colors.sort()

# for colors in colors:
#     if colors > 50:
#         print(colors)



colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
colors.append(10)
colors.sort()

for colors in colors:
    if isinstance(colors,int):
        print(colors)