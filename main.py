from urllib.parse import urljoin
import os
import shutil
import webbrowser
from PIL import Image
from bs4 import BeautifulSoup
from form import get_all_forms, get_form_details, session
from imgdownload import get_all_images, download
from metadata import get_metadata


imagename = "3.jpg"
url = "https://www.techpowerup.org/upload"
# url = "https://www.exifremove.com/"


if os.path.isdir('./images'):
    shutil.rmtree('./images')

first_form = get_all_forms(url)[0]
form_details = get_form_details(first_form)

uploadfile = open(imagename, "rb")
myImage = Image.open(imagename)
data = {}
for input_tag in form_details["inputs"]:
    if input_tag["type"] == "hidden":
        data[input_tag["name"]] = input_tag["value"]
    elif input_tag["type"] != "submit" and input_tag["type"] == "file":

        data[input_tag["name"]] = uploadfile


if form_details["action"] != "none":
    url = urljoin(url, form_details["action"])
    print(form_details["action"])

if form_details["method"] == "post":
    res = session.post(url, files=data)
elif form_details["method"] == "get":
    res = session.get(url, params=data)

soup = BeautifulSoup(res.content, "html.parser")

for link in soup.find_all("link"):
    try:
        link.attrs["href"] = urljoin(url, link.attrs["href"])
    except:
        pass
for script in soup.find_all("script"):
    try:
        script.attrs["src"] = urljoin(url, script.attrs["src"])
    except:
        pass
for img in soup.find_all("img"):
    try:
        img.attrs["src"] = urljoin(url, img.attrs["src"])
    except:
        pass
for a in soup.find_all("a"):
    try:
        a.attrs["href"] = urljoin(url, a.attrs["href"])
    except:
        pass

open("page.html", "w").write(str(soup))

imageformat = myImage.format

if imageformat == "JPEG":
    imageformat = "jpg"

imgs = get_all_images("page.html")
for img in imgs:
    try:
        if imageformat.lower() in img:
            download(img, 'images')
    except:
        print('Couldent download any images!!!')

# webbrowser.open("page.html")
webbrowser.open(res.url)
print('\n\n********************************************')
imagemeta = get_metadata(imagename)
print('Before upload:')
if(imagemeta):
    print(get_metadata(imagename))
else:
    print('No metadata found!!!')


imagename = os.listdir('./images')[0]

print('\n\nAfter upload:')
if(imagemeta):
    print(get_metadata('./images/' + imagename))
else:
    print('No metadata found!!!')
print('********************************************')
