"""
This file contains the colors extracted from the Hirst's dot painting
"""

import colorgram

# Replace the file path with the path of the image on your system
color_palette = colorgram.extract('hirst_painting.jpg', 30)
rgb_colors = []

for color in color_palette:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)

# This is the output of rgb_colors
colors_list = [
    (131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157),
    (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55),
    (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110),
    (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)
]
