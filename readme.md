# Django Website Monitor

Python website monitoring app. The app makes asynchronous requests to the websites added for the user
 and keeps detailed logs of the responses. If a status code different from 200/301/302 is detected an email
will be sent to the user. The crons are automated with celery and can be easily edited or scaled if needed. 

# Table of contents
* [Installation](#Installation)
* [Setup](#Setup)
* [Technologies](#Technologies)
* [Contibuting](#Contributing)
* [License](#License)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements located in requirements.txt.

```bash
pip install -r requirements.txt
```

#### Postgre setup

The project requires [PostgreSQL](https://www.postgresql.org/download/) . In the link it can be found available 
for all operating systems. In order to create and manage the database it is also needed to download a sql client for example
[PgAdmin](https://www.pgadmin.org/download/).

## Setup

1. Clone the repository.
```bash
git clone git@github.com:LilkoPetkov/python-web-project.git
``````
2.  Rename the sample_env file to .env and reconfigure it with your local postgres details.
3.  Run the migrations
```bash
python manage.py makemigrations
python manage.py migrate
``````
4. Navigate to the python robomonitor folder and run the app.
```bash
python manage.py runserver
``````
5. Once the app is started, we need to run the celery worker so the automated tasks can be executed
```bash
celery -A robomonitor worker -l info
``````
6. Once the worker is enabled, we enable the beat
```bash
celery -A robomonitor beat -l info
``````



## Technologies
 - Python 3.8 / 3.11
 - pgAdmin 4 v6.21
 - PostgreSQL 13.10 
 - HTML
 - CSS
 - Celery 5.3.1 (emerald-rush)
 - Redis server v=7.0.12

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
