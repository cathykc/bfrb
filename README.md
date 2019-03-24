# BFRB

## Start the application

### Environment variables
```
source .envrc
```
or do yourself a favor and install direnv

In different terminal windows:

### Frontend
```
cd client
yarn install
yarn start
```

Check that the frontend is running by going to http://localhost:3000

### Backend
```
cd server
source env/bin/activate
python app.py run_server
```

Check that the api is serving responses by going to http://localhost:5100/api

## Set up

### Database
```
createdb bfrb_dev
cd server
python manage.py db upgrade
```

### Backend requirements
```
virtualenv env
source activate env/bin/activate
pip install -r requirements.txt
```
