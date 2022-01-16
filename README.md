
# flask-boilerplate


## Development commands


### Setup from zsh:

```
# Clone
git clone https://github.com/asiftyro/flask-boilerplate.git

# Change dir
cd flask-boilerplate

# Create virtual env
python3 -m venv venv
# Or,
virtualenv venv -p python3

# Activate virtual env
source venv/bin/activate

# Install packages
pip3 install -r requirements.txt

# Set env variables
export FLASK_APP=flaskr
export FLASK_ENV=development

# Initialize database
flask init-db
```

### Run app

```
flask run
# Or,
flask run --host=0.0.0.0 --port=8888
# Or,
python3 -m flask run
```

### Tests and Coverage

```
# Run tests
pytest

# Measure the code coverage of tests
coverage run -m pytest

# View a simple coverage report in the terminal
coverage report

# Generate and view HTML coverage in browser
coverage html
open htmlcov/index.html
```
  
### Misc  

```
# Deactivate venv
deactivate

# Remove all packages installed by pip3
pip3 freeze | xargs pip3 uninstall -y
```

  
--------------------------

  
  
## ToDo:

- [x] Bootsrap CSS integration
    - [x] Upgrade templates
- [ ] WTForms integration
    - [x] Implement Flask-WTF
    - [x] Form Validation
	- [ ] Re/Captcha implementation
	- [ ] WYSIWYG implementation
	- [-] Update existing forms
	- [ ] Admin CRUD
- [ ] SQLAlchemy integration
- [ ] DB Migration system integration
- [ ] Mail integration
- [ ] Configuration file implementation 
  - [ ] development and production profiles
  - [ ] site-wise settings
  - [ ] credentials, keys
- [ ] MariaDB integration
- [ ] WSGI/ASGI implementation
- [ ] Deployment workflow creation
- [ ] Standard secured User management and ACL implementation  
	- [ ]  Registration
	- [ ]  Verification
	- [ ]  Authentication
	- [ ]  2FA
	- [ ]  Roles
- [ ] Google analytics integration
- [ ] Server and Cient side Datatables integration
- [X] Test implementation
- [x] Feather icon implementation
- [x] 404 page
- [ ] Logging
- [ ] Flash message with criticality
- [ ] Time zone
- [x] Blueprint auto loading


----------------------

#### Notes:
 - Test settings are in setup.cfg


#### References:

- https://flask.palletsprojects.com/en/2.0.x/
- https://bootstrap-flask.readthedocs.io/
- https://flask.palletsprojects.com/en/2.0.x/tutorial/
- https://feathericons.com/
- https://flask-wtf.readthedocs.io/
- https://wtforms.readthedocs.io/en/3.0.x/


----------------------


##### Based on The Application Factory Pattern shown in official [Flask Tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/)