import os
import datetime
from PIL import Image, ExifTags

lis1=[]
lis2=[]
for root, dirs, files in os.walk("."):
    for i in files:
        print(i)
        if i[-3:] in ("JPG"):
            with Image.open(i) as img:
                img_exif=img.getexif()
                print(i, " ", img_exif[306], " ", i[-8:-4])
                fname = "IMG_"+img_exif[306][:4]+img_exif[306][5:7]+img_exif[306][8:10]+"_"+img_exif[306][11:13]+img_exif[306][14:16]+img_exif[306][17:19]+"_"+i[-8:]
                lis1.append({i:fname})
print(lis1)
for i in lis1:
    for key, val in i.items():
        try:
            os.rename(key, val)
            print("Renamed ", key)
        except:
            lis2.append(key)
print(lis2)
