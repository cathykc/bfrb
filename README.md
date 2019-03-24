# BFRB

A configurable chatbot digital therapeutic that augments therapists during habit-reversal therapy for hair pulling (Trichotillomania) and other impulse-control disorders.

### Configuring a CBT treatment
![image](https://cl.ly/e1ab9b826355/Screen%252520Recording%2525202019-03-24%252520at%25252011.31%252520AM.gif)

### Chatbot experience
| ![image](https://d2ddoduugvun08.cloudfront.net/items/3f2L0A461i2S2J2N163G/Screen%20Recording%202019-03-24%20at%2012.04%20PM.gif) | ![image](https://d2ddoduugvun08.cloudfront.net/items/3b140d2u462i3X3R1f2K/Screen%20Recording%202019-03-24%20at%2012.05%20PM.gif) |

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
