# youtube-crawler

### Requirements
* python(v 2.7)
* postgresql

### Installation

* run the following command to clone the repo
```git clone https://github.com/Abdo-Sameh/youtube-crawler && cd youtube-crawler``` then install the requirements through ``` pip install -r requirements.txt```
* rename file ```.env.sample``` to ```.env```

### Setting up database
* Create a database through this command ```sudo -u [name_of_user] createdb [name_of_database]```, then change database URL from ```.env```
file.
* run ```python manage.py db upgrade``` to build database and migrate.

### Running
To run flask app ```FLASK_APP=app.py flask run```

### How to use
| Method |    URL    |  Params          |
| ------ | --------- |----------        |
| Get    | /playlist | ```playlistId``` | 
| Get    | /channel  | ```channelId```  |

***Note***: To run cron job just run ```python cron_schedule.py```