# Travelogue
* [Link to site](https://travelogue.herokuapp.com)
* Travelogue is for people that enjoy to travel but mainly for my partner who is a flight attendant so she can plan and track her trips!

## Tech Used
```
Django
PostgreSQL
Python
Bootstrap
Heroku
```

## Installation
1. Install the virtual environment: 
Open your terminal and run this to install the virtualenv package.
```
pip install virtualenv
```
2. Create the virtual environment: 
Run the following command in your terminal, replacing myenv with the desired name of your virtual environment:
```
virtualenv myenv 
```
3. Activate the virtual environment: 
Run the following command in your terminal:
```
source myenv/bin/activate
```
4. Once the virtual environment is activated, any packages you install using pip will be installed in the virtual environment and will not affect other projects on your system. To deactivate the virtual environment, simply run
```
deactivate.
```
5. Install dependencies: 
Navigate to the project directory and run this command to install all the required dependencies.
```
pip install -r requirements.txt
```
6. Configure the settings: 
Open the settings.py file and make sure the database, email and other configurations are set up properly.

7. Run migrations by running this command to create the necessary tables in your database.
```
python manage.py migrate
```

8. Start the development server: 
Use this command to start the development server and access your application at http://localhost:8000.
```
python manage.py runserver
```

## Usage
### Home
All you have to do is Sign In/Up or click to start your first trip.
![Home](https://i.gyazo.com/a58e1fdb0a1a097b63abbab19b7741cd.jpg)
### Sign In
You can choose to create an account with Google or Sign in if you are an existing user.
![Sign In](https://i.gyazo.com/16e787fb06a09bb15dc5ac8b7ce04c52.jpg)
### Sign Up
You can also choose to sign up without connecting your Google account.
![Sign Up](https://i.gyazo.com/6334b4ea1373aefad310183672a5b855.jpg)
### Start Trip
Once you enter the Destination, Start and End Dates you can then begin planning. 
![Start Trip](https://i.gyazo.com/c2ab30fb76970dc1477d69c199e609b8.jpg)
### Plan Trip
There is a section to organize your budgets by category, as well as a section to create lists of your liking.
e.g. Reminders, Things to Bring, Activities to do
![Plan Trip](https://i.gyazo.com/316fe76c68ea3f6f8119e050635a5ec3.jpg)

## Stretch Goals
* Trip Weather
* Google Calendar
* Currency Exchange
* Google Maps

## Planning

[PLANNING.md](https://github.com/efrainenc/capstone/blob/main/PLANNING.md)
