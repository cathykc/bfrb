# BFRB

## Start the application

### Environment variables
```
source .envrc
```

In different terminal windows:

### Frontend
```
cd client
cd yarn start
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
# Run migrations - TO DO
```

### Backend requirements
```
virtualenv env
source activate env/bin/activate
cd server
pip install -r requirements.txt
```
