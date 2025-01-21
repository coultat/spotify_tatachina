<h1>Django API that fetches Spotify Artists through the their artist_id</h1>

<h2>Django app to fetch and store artist information from the Spotify API using their ID.</h2>

How does it work:
- Clone this repository
- run the migrations
 ```bash
python manage.py makemigrations; python manage.py migrate
```
- Run the localhost server
 ```bash
python manage.py runserver
```
- Send a get request to the endpoint http://127.0.0.1:8000/spotify/artists/ with the following data
{"artist_id": "your artist id"}
- A response will be sent back with the data of the artist

https://app.diagrams.net/#G1AXrWryQ8Ej45wIwKQ1KMKLwowgDT7CBA

<h2>Technical Requirements</h2>
- Django
- djangorestframework
- httpx
- psycopg2
- django-environ

For more information about the versions, please check the requirements.txt

<h2>Setting up the environment </h2>
- Clone this repository
- Create the environment and install the requirements

```bash 
python -m venv .env 
source .env/bin/activate
pip install requirements.txt- 
```

<h2>More info for contributors and users</h2>
This is a personal repository for learning purposes. All feedbacks are welcome :-)

<h2>Known issues</h2>
- [X] Missing timeout in the client <br>
- [X] Push migrations<br>
- [x] README.md
- [x] Fix serializers structure
- [x] Fix db structure
- [] Add tests
- [x] Add cache