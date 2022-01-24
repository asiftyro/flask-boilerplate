
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
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=True;

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

# Set ENV and run flask
export FLASK_APP=app;export FLASK_ENV=development;export FLASK_DEBUG=True;flask run;
```


--------------------------

  
  
## ToDo:

- [x] Bootsrap CSS integration
    - [x] Upgrade templates
- [ ] WTForms integration
    - [x] Implement Flask-WTF
    - [x] Form Validation
	- [ ] Re/Captcha implementation
	- [-] WYSIWYG implementation
	- [-] Update existing forms
    	- [x] Login
    	- [ ] Register
- [-] Admin 
  	- [x] Create Post
  	- [x] Edit Post
  	- [x] View Post
  	- [x] View All Post
	- [ ] File Upload
	- [x] List Menu
	- [x] Edit Menu
	- [x] Admin Home
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
- [x] Test implementation
- [x] Feather icon implementation
- [x] 404 page
- [ ] 500 page
- [ ] Logging
- [x] Flash message with criticality
- [x] Favicon
- [x] Sitename from config
- [x] Time zone
- [x] Blueprint auto loading
- [ ] Code formatter/prettyfier to show content
- [ ] Code auto format in textarea
- [x] Table render macro
- [x] Menu item rendering macro
- [ ] Route List
- [ ] Insert template for content type, e.g. hero, slider etc
- [-] Create model helper methods
  - [-] find_or_abort
  - [ ] insert
  - [ ] delete
  - [ ] update



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
- TinyMCE 5.10.2 (2021-11-17) https://www.tiny.cloud/docs/

----------------------


##### Based on The Application Factory Pattern shown in official [Flask Tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/)