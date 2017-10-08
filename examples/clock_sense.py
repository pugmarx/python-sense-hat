###################
## Courtesy: https://yjlo.xyz/blog/design-a-digital-clock-on-raspberry-pi-sense-hat/
##################

from sense_hat import SenseHat
import datetime
import time

sense = SenseHat()
sense.low_light = True
sense.rotation = 180

# unit: 60/29
u = 60.0 / 29

zero = [[0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0]]
one = [[0, 0, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0],
       [0, 0, 1, 1, 1, 0]]
two = [[0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0],
       [0, 1, 1, 1, 1, 0]]
three = [[0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0]]
four = [[0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
five = [[0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0]]
six = [[0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0],
       [0, 0, 1, 1, 0, 0]]
seven = [[0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0]]
eight = [[0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0],
         [0, 0, 1, 1, 0, 0]]
nine = [[0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0]]
ten = [[0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1],
       [0, 1, 0, 0, 1, 0]]
eleven = [[0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0],
          [0, 1, 0, 0, 1, 0]]
twelve = [[0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0],
          [0, 1, 0, 1, 1, 1]]

nums = [zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]

# hour background color
z = [0, 0, 0]

# hour number color
#w = [255, 255, 255]
w = [50, 50, 50]

# minute background color
e = [0, 0, 0]

# minute dot color
x = [ 50, 50, 0]


def row_one(m):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    if m > u * 4 and m < u * 25:
        result = [0, 0, 0, 0, 1, 1, 1, 1]
    else:
        if m < u:
            result = [0, 0, 0, 0, 0, 0, 0, 0]
        elif m < u * 2:
            result = [0, 0, 0, 0, 1, 0, 0, 0]
        elif m < u * 3:
            result = [0, 0, 0, 0, 1, 1, 0, 0]
        elif m < u * 4:
            result = [0, 0, 0, 0, 1, 1, 1, 0]
        elif m < u * 25:
            result = [0, 0, 0, 0, 1, 1, 1, 1]
        elif m < u * 26:
            result = [1, 0, 0, 0, 1, 1, 1, 1]
        elif m < u * 27:
            result = [1, 1, 0, 0, 1, 1, 1, 1]
        elif m < u * 28:
            result = [1, 1, 1, 0, 1, 1, 1, 1]
        else:
            result = [1, 1, 1, 1, 1, 1, 1, 1]
    return result


def row_eight(m):
    result = [1, 1, 1, 1, 1, 1, 1, 1]
    if m < u * 18:
        if m < u * 11:
            result = [0, 0, 0, 0, 0, 0, 0, 0]
        elif m < u * 12:
            result = [0, 0, 0, 0, 0, 0, 0, 1]
        elif m < u * 13:
            result = [0, 0, 0, 0, 0, 0, 1, 1]
        elif m < u * 14:
            result = [0, 0, 0, 0, 0, 1, 1, 1]
        elif m < u * 15:
            result = [0, 0, 0, 0, 1, 1, 1, 1]
        elif m < u * 16:
            result = [0, 0, 0, 1, 1, 1, 1, 1]
        elif m < u * 17:
            result = [0, 0, 1, 1, 1, 1, 1, 1]
        else:
            result = [0, 1, 1, 1, 1, 1, 1, 1]
    return result


def convert_to_color(arr, background, color):
    return [background if j == 0 else color for j in arr]


def update_clock(hh, mm):
    if hh > 12:
        hh = hh - 12

    img = []

    # row 1
    row1 = row_one(mm)
    img.extend(convert_to_color(row1, e, x))

    # row 2-7
    for i in range(6):
        if mm > (u * (24 - i)):
            img.append(x)
        else:
            img.append(e)

        # hour number
        img.extend(convert_to_color(nums[hh][i], z, w))

        if mm > (u * (5 + i)):
            img.append(x)
        else:
            img.append(e)

    # row 8
    row8 = row_eight(mm)
    img.extend(convert_to_color(row8, e, x))

    sense.set_pixels(img)


def sense_vals():
#    while True:
    yellow = (150, 150, 0)
    blue = (0, 0, 100)

    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()

    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    msg = "Temperature = {0}, Pressure = {1}, Humidity = {2}".format(t,p,h)
    sense.show_message(msg, scroll_speed=0.09, text_colour=yellow, back_colour=blue)


try:
    while True:
        now = datetime.datetime.now()
        update_clock(now.hour, now.minute * 1.0)
        time.sleep(30)
        sense_vals()
        #time.sleep(20)
except KeyboardInterrupt:
    print 'Closed.'
    sense.clear()
