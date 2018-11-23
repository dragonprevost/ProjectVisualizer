# Project Visualizer
This is the backend to Vlyzer. A software platform that provides visual representation of ongoing projects on github. 
## Getting Started
The backend of Vlyzer is written in Python3 using the django rest framework. Providing an interface for a custom data base designed to store user data and account settings. 

### Dependencies
- Python3 installs - ( [mac](https://www.python.org/downloads/mac-osx/) / [linux](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux-python.html) / [windows](https://www.python.org/downloads/) )
- DjangoRestFramework [install]( https://www.django-rest-framework.org/#installation )



### Configuring Database
For the purpose of producing minimal functionality while displaying the use of django rest framework the data base has been configured with only one table that holds a list of repositries. This list may be seen as a portfolio of ongoing projects for person in position of leadership.
### Starting Server
To start the Rest API server follow these instructions
```sh
cd ~
git clone https://github.com/dragonprevost/vlyzer_backend.git
cd vlyzer_backend/
python3 manage.py runserver
```
### Testing the Rest API Server
After cloning this repository there will be 2 default repositories stored in the database.You can confirm that your server is running properly by making a get request to `http://localhost:8000/repos/`. I reccomend using the `httpie` command line tool if using mac or linux. 
```json
$ http http://localhost:8000/repos/

HTTP/1.1 200 OK
Content-Length: 354
Content-Type: application/json
Date: Fri, 23 Nov 2018 19:10:39 GMT
Server: WSGIServer/0.2 CPython/3.6.7
X-Frame-Options: SAMEORIGIN

[
    {
        "branch": "master",
        "id": 5,
        "repo_name": "vlyzer_backend",
        "title": "vlyzer_backend",
        "url": "https://github.com/dragonprevost/vlyzer_backend",
        "user_name": "dragonprevost"
    },
    {
        "branch": "master",
        "id": 6,
        "repo_name": "motion-service",
        "title": "motion service",
        "url": "https://github.com/dragonprevost/motion-service",
        "user_name": "dragonprevost"
    }
]


```
