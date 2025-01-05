# my_python_blogapp02

# Steps required to start and run the application

Install python 12 or higher, venv, Django, sqlite3, etc.

# Set up a virtual environment

$ rm -r myvenv

$ python3 -m venv myvenv

$ source myvenv/bin/activate

# Reinstall pip in the virtual environment, upgrade, check, install Django, check

$ python3 -m ensurepip --upgrade

$ pip install --upgrade pip

$ pip --version

$ pip install django

$ python3 -m django --version

# Start by specifying the IP address and port

$ python3 manage.py runserver 127.0.0.1:8003

Access http://127.0.0.1:8003/blog/ in your browser

Check the dummy data
