# workshop Django Web Framework
Just follow the instalation steps.
- Django & python-pip steps
    - [Fedora Installation](#fedora-installation)
    - [Ubuntu Installation](#ubuntu-installation)


## Fedora Installation
In your terminal Move to root
```
    # yum-y install python-pip
    # sudo dnf install pyhton-virtualenv
```
Move to your desired directory and type
```
    $ virtualenv .
```

## Ubuntu Installation
```
    $ sudo apt-get update
```
### For python 2.*
```
    $ sudo apt-get install python-pip
    $ pip install virtualenv
    $ virtualenv trydjango
    $ pip install django==1.11
```
### For python 3.*
```
    $ sudo apt-get install python3-pip
    $ pip3 install virtualenv
    $ virtualenv -p python3 trydjango
    $ pip3 install django==1.11
```

Then clone the project and install packages with `requirements.txt`
```
    $ pip install -r requirements.txt
    $ cd project
```

change the SMTP email configuration in `settings.py`
```
EMAIL_HOST = 'smtp.gmail.com'  # since you are using a gmail account
EMAIL_PORT = 587  # Gmail SMTP port for TLS
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
```
Finally use the following commands to run the project 
```
    $ python manage.py runserver
```

