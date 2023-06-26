# Metropark_02

This is Metropark system.


### Run the project locally:


In order to run the project locally, the developer should add the following directories and files to the main project folder :

.envs
├── .local
│ ├── .django
│ └── .postgres
.env



Without these two files, Docker will not have access to the keys, and without them, it will not be possible to access the database. Please request those files from the project manager (tzurjob09@gmail.com).



   Then:
    1. Create a virtualenv: $ python3.11 -m venv <virtual env path>
    2. Activate the virtualenv you have just created: $ source <virtual env path>/bin/activate
    3. Install all the necesary dependecies to your virtualenv: $ pip install -r requirements/local.txt




The next step is to build an image and then build a container. 

To build the Image run in the terminal:
1. $ docker-compose -f local.yml build

Then to build and run the container run in the terminal:
2. docker-compose -f local.yml up



### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message in your console. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.




[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).