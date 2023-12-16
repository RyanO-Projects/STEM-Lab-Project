# COSC-2418 Final Project

## About:

This is a project for hosting a website for the Casper College STEM Learning Center. It provides a calendar that shows when tutors are available, and what subjects they tutor. It also allows for signing in and out so that hours can be logged. Although it is specific to Casper College, it can easily be altered for other uses.

## Features:

- Sign in/ Sign out functionality
- A calendar that displays tutoring hours
- A homepage that combines these functions into one place

## Installation:

1. Make sure that Python 3 is installed

    Open a terminal to check and see if python is properly installed:

                python --version

    If Python is not installed, or not on version 3, visit the [Python Website](https://www.python.org/downloads/) to download

    If you are on Windows and have installed Python but it is still not working, make sure that Python has been added to Windows PATH.
    [Here is a useful tutorial for adding Python to your PATH](https://www.geeksforgeeks.org/how-to-add-python-to-windows-path/)

    If it is still not working, use "py" instead of "python" when entering commands into your terminal, like so:

                py --version

2. Clone repository or download files through Github

3. Make sure that requirements are met

    In your terminal:

    Update pip

                python -m pip install --upgrade pip

    and install required addons
    
                pip install -r requirements.txt

4. Make sure you are in the proper directory, and make migrations:

    In your terminal:

                python manage.py makemigrations
                python manage.py migrate

5. Run server

    In your terminal:

                python manage.py runserver

6. Visit the website

    Visit [this link](http://127.0.0.1:8000/) to see it

## Bug List

- It's not done yet.