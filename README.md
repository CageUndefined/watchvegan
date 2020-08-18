# Watchvegan

This repo stores the codebase for the watchvegan website founded by cageundefined. It runs on the Python Django stack with a sqllite3 database. The objective of this website is to automatically publish whitelisted videos from Youtube, Vimeo, and other sources on a page for people to watch.

## Installation

Create a virtual environment for the codebase. [Pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) is recommended. The following steps describe the process to create a virtual environment using pyenv-virtualenv for watchvegan. If you have not installed pyenv-virtualenv follow [these instructinos](https://github.com/pyenv/pyenv-virtualenv#installation)

1. Install the python version to pyenv. This will ensure you are using Python 3.8.2 in the virtualenvironment created for step two.
```bash
pyenv install 3.8.2
```
2. Create a virtualenv using the python base we just installed. You can name the virtualenvironment anything you want. In this example the name of the virtualenv is `watchvegan`
```bash
pyenv virtualenv 3.8.2 watchvegan
```
3. Activate the virtualenv. This will ensure you are using the environment we just created when installing the pip packages required for watchvegan.
```bash
pyenv activate watchvegan
```
4.  If you would like the virtualenv to automatically activate when you navigate into the watchvegan directory, create a file in the root directory of watchvegan called `.python-version`. Inside that file type the name of the virtualenv and save it. Next time you navigate to the watchvegan directory, the virtualenv created in step two will activate automatically.

5. Install the required pip packages onto the active virtualenv
```bash
pip install -r requirements.txt
```
## Running watchvegan

1. Verify that the virtualenv is active
```bash
pyenv activate watchvegan
```
2. Apply any new migrations. On a fresh install, this will create the sqlite database on the root directory of this codebase.
```bash
python manage.py migrate
```
3. Start the server
```bash
python manage.py runserver
```
4. You can now access the website locally at `http://127.0.0.1:8000/`. The admin interface is accesible at `http://127.0.0.1:8000/admin`
## Creating a superuser
1. To be able to log into the admin portal, create a superuser
```bash
python manage.py createsuperuser
```
2. Enter the fields from the prompt. Only username and password are required. Password letters will not show up when you type.
```bash
➜  python manage.py createsuperuser
Username (leave blank to use 'nick'): admin
Email address: 
Password: 
Password (again): 
Superuser created successfully.
```
3. You can now log into the admin portal using the credentials you created in the previous step
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>