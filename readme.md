# Project Visualizer
This is the backend to Vlyzer. A software platform that provides visual representation of ongoing projects on github. 
## Getting Started
The backend of Vlyzer is written in Python3 using the django rest framework. Providing an interface for a custom data base designed to store user data and account settings. 

### Dependencies
- Python3
- DjangoRestFramework


### Configuring Database
For the purpose of producing minimal functionality while displaying the use of django rest framework the data base has been configured with only one table that holds a list of repositries. This list may be seen as a portfolio of ongoing projects for person in position of leadership.
### Starting Server
To start the Rest API server follow these instructions
```sh
cd ~
git clone https://github.com/dragonprevost/vlyzer_backend.git
cd vlyzer_backend/
python3 manage.py runserver

