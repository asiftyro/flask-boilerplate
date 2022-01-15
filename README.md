
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
pip install -r requirements.txt
### Set env variables
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
### Initialize database
flask init-db
### Run app
flask run
```

  

--------------------------

  
  

```
### Deactivate venv
deactivate
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