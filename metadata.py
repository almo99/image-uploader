from PIL import Image
from PIL.ExifTags import TAGS


def get_metadata(imagename):
    image = Image.open(imagename)
    iccdata = image.info
    alldata = ""

    for tag_id in iccdata:
        tag = TAGS.get(tag_id, tag_id)
        alldata = str(tag) + ' - ' + alldata
    return alldata
