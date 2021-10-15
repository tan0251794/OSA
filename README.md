# OSA
```diff
! Oversea Shipping API
```

## Deployed at: https://osa-api.herokuapp.com/

## Guide to run the project locally: 
- install virtualenv: python -m venv venv
- active virtualenv: source venv/bin/activate
- (venv) pip install -r requirements.txt
- (venv) python manage.py makemigrations
- (venv) python manage.py migrate 
- (venv) python manage.py runserver 


## API PATH: 
+ ORDER:
- detail: http://127.0.0.1:8000/api/order/<:id>/
- create: http://127.0.0.1:8000/api/order/create/
- update: http://127.0.0.1:8000/api/order/<:id>/edit/
- delete: http://127.0.0.1:8000/api/order/<:id>/delete/

+ PRODUCT:
- list:   http://127.0.0.1:8000/api/product/
- detail: http://127.0.0.1:8000/api/product/<:id>/
- create: http://127.0.0.1:8000/api/product/create/
- update: http://127.0.0.1:8000/api/product/<:id>/edit/
- delete: http://127.0.0.1:8000/api/product/<:id>/delete/

+ PACK:
- list:   http://127.0.0.1:8000/api/pack/
- detail: http://127.0.0.1:8000/api/pack/<:id>/
- create: http://127.0.0.1:8000/api/pack/create/
- update: http://127.0.0.1:8000/api/pack/<:id>/edit/
- delete: http://127.0.0.1:8000/api/pack/<:id>/delete/

## BACKEND SYSTEM PATH: 
+ order management：   http://127.0.0.1:8000/
+ product management： http://127.0.0.1:8000/product/
+ pack management：    http://127.0.0.1:8000/pack/

## ADMIN SITE:
+ admin: http://127.0.0.1:8000/admin/
+ auth:  http://127.0.0.1:8000/api/login/


## .app file for ios: https://expo.dev/accounts/jasonisme/projects/osa-application/builds/9c3e71db-0137-4683-b0e2-5cc3aaef6cca
## Frontend: https://github.com/tan0251794/OSA-Application
