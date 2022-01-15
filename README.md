
# flask-boilerplate

  
### Setup from zsh:


```
### Clone
git clone https://github.com/asiftyro/flask-boilerplate.git
### Change dir
cd flask-boilerplate
### Create virtual env
python3 -m venv venv
### Activate virtual env
source venv/bin/activate
### Install packages
pip3 install -r requirements.txt
### Set env variables
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
### Initialize database
flask init-db
```

### Run app

```
flask run
```

### Tests and Coverage
```
### Run tests
pytest
### Measure the code coverage of tests
coverage run -m pytest
### View a simple coverage report in the terminal
coverage report
### Generate and view HTML coverage in browser
coverage html
open htmlcov/index.html
```


--------------------------

  
  
```
### Deactivate venv
deactivate
### Remove all packages installed by pip3
pip3 freeze | xargs pip3 uninstall -y
```

  
--------------------------

  
  
### TODO:

- [ ] Bootsrap CSS integration
    - [ ] Upgrade templates
- [ ] WTForms integration
	- [ ] Recaptcha implementation
	- [ ] WYSIWYG implementation
	- [ ] Update existing forms
- [ ] SQLAlchemy integration
- [ ] DB Migration system integration
- [ ] Mail integration
- [ ] Configuration file implementation (development and production profiles)
- [ ] MariaDB integration
- [ ] WSGI/ASGI implementation
- [ ] Deployment workflow creation
- [ ] Standard secured User management and ACL implementation  
	- [ ] Registration
	- [ ]  Verification
	- [ ]  Authentication
	- [ ]  2FA
	- [ ]  Roles
- [ ] Google analytics integration
- [ ] Server and Cient side Datatables integration
- [X] Test implementation


----------------------

##### Based on The Application Factory Pattern shown in official [Flask Tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/)