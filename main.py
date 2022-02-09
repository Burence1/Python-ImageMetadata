from PIL import Image
from PIL.ExifTags import TAGS

#Method 1
# extract EXIF data
exifdata = Image.open("images/IMG_6317.JPG")._getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")


#Method 2

# img = Image.open("images/IMG_6317.JPG")
# exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

# print(exif)
