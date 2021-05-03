# Shopify Internship Challenge

## Installation

### Prerequisite

To run this Image repository application you need <b>Python 3.6</b> or later and <b>NodeJS</b> installed on your machine.

### Getting started

To install the project, run the following commands in the command line:

```
cd BE
pip install -r requirements.txt
```

```
cd FE
npm i
```
Disclaimer, this app is made to have the backend and frontend run locally.

## Start the application

To start the application, you need to start the backend and the frontend servers, to do so, you need to run the following commands :

#### Start Backend server
```
python BE/shopictures/manage.py makemigrations shopictures
python BE/shopictures/manage.py migrate
python BE/shopictures/manage.py runserver
```

#### Start Frontend server
```
cd FE
npm run build
npm run serve
```

In your browser, get the page:
 http://localhost:8080/

## How to use the app

There are two features to the Shopictures app: 
- Search Images
- Upload Images

### Uploading an image

1. To upload an picture, click on the Upload button at the top right of the window.
2. Enter a name, a price for your image and select an image from your computer.
3. Press the submit button.

### Searching images

1. To search for images, click the search button at the top right of the window.
2. Select the <em>Search for a image</em> field.
3. Enter a keyword.
4. Press the <b>Enter</b> key.


## Running the test cases
```
python BE/shopictures/manage.py test
```