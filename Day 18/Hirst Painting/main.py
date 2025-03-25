import colorgram

colours_from_image = (colorgram.extract('image.jpg', 10))
colour_list = []

for colour_number in range(10):
    current_colour = colours_from_image[colour_number]
    rgb = (current_colour.rgb[0], current_colour.rgb[1], current_colour.rgb[2])
    colour_list.append(rgb)

print(colour_list)