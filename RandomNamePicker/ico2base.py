import base64

open_icon = open('C:\\Users\\rbesemer\\PycharmProjects\\pythonProject\\RandomNamePicker\\images\\Icons8-Ios7-Gaming'
                 '-Dice.ico', "rb")  # your ico img
b64str = base64.b64encode(open_icon.read())
open_icon.close()
write_data = ("img = %s" % b64str)
f = open("icon.py", "w+")
f.write(write_data)
f.close()
