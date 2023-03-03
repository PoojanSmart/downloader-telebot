import os

for i in os.listdir():
    if i.split(".")[-1] == "mp4":
        os.unlink(i)