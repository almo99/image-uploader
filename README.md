## HOW TO RUN PROGRAM

- Install latest version of python from https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe
- Install below packages with pip:
  - beautifulsoup4==4.9.1: for parsing html and forms
  - Pillow==7.2.0: for extracting image metadata
  - requests-html==0.10.0: for requesting urls and uploading to and dowloanding files from a url
  - urllib3==1.25.9: utility package
  - tqdm==4.45.0
- Command for installing packages:
  python -m pip install -r requirements.txt
- In main.py specify imagename and url address
- In root project directory from your terminal run this command:
  python main.py

## HOW IT WORKS

- form.py module has two functions:
  - get_all_forms: for getting forms from a url
  - get_fomr_details: for getting form detail

The two functions above are using beatifulsoup4 and requests_html packages

- imagedownload.py module downloads the uploaded image from given url
- metadata.py module checks the images and prints its metadata if availalbe using PIL(Pillow) package

- main.py has all these three modules imported

first we check our image metadata
then we extract the form from the given url, then we get the details of that form(i.e form inputs)
then we send our image using specified method in form to specified action in the form
after that we check the response url and download all relevant images
then we check the downloaded image metadata and print it along with metadate of our picture before upload
