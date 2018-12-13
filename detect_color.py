from PIL import Image
import sys
import cv2
import numpy as np


def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    return most_frequent_pixel[1]


def save(result):
    sample = Image.new("RGB", (200, 200,), result)
    sample.save("result2.jpg")


def main():
    img = Image.open('./Sports/shoe1.jpg')
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("img2.jpg", "PNG")

    img2 = Image.open("img2.jpg")

    result = most_frequent_colour(img2)
    print(result)

    save(result) 


if __name__ == "__main__":
    main()