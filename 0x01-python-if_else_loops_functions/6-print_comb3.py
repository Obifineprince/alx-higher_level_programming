#!/usr/bin/python3
for j in range(1, 90):
    if j / 10 > j % 10:
        continue
    else:
        if (j != 89):
            print("{:02}".format(j), end=", ")
        else:
            print("{}".format(j))
