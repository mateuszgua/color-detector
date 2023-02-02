import argparse
import cv2
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)

clicked = False
r = g = b = xpos = ypos = 0

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv("colors.csv", names=index, header=None)