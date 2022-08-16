# weather
Django Weather Rest API

## Configuring Environment Variables
Environment variables should be set on your bare-metal computer before the app is run.

```bash
export DJANGO_SETTINGS_MODULE="settings.dev_settings"
export SECRET_KEY="<your secret key>"
export BASE_WEATHER_API_URL="http://api.weatherapi.com/v1/history.json"
export WEATHER_API_KEY="<your external api key>"
```

Ideally i should not be exposing environmnet variables to the outside world but for the purposes
of this assigmnent I have already set this environment variables in the `api.env` file in the 
`env` folder

When you run the app using docker-compose these enviroment variables will be set in the running
docker container 

## Running the app (on docker-compose)

### Prerequisites
1. [Install docker](https://docs.docker.com/engine/install/)
2. [Install docker-compose](https://docs.docker.com/compose/install/)


### Running the app
1. Clone the git repo.

    ```bash
    git clone git@github.com:sitati-elsis/weather.git
    ```
2. `cd` into the repo you have just cloned.
    ```bash
    cd weather/
    ```
3. Use the following command to run the app
    ```bash
    docker-compose up
    ```

You do not have to set any environment variables since I have already told docker where to 
get the environment variables



## Running the app (on your bare-metal machine)
### Prerequisites

Makes sure environment variables describled earlier are set on your bare-metal computer before the app is run.

1. [Install virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
2. Create a virtual environment
    ```bash
    # an example where virtualenv is named "weather"
    virtualenv weather
    ```
3. Activate the virtual environment
    ```bash
    # an example where virtualenv is named "weather"
    source weather/bin/activate
    ```
3. Install app dependencies
    ```bash
    pip install -r requirements.txt
    ```
### Running the app
1. Run the app using the following command.
    ```bash
    python manage.py runserver
    ```

## API Documentation
API Documentation can be accessed through a GET request to the following route.
```
http://localhost:8000/api/docs/
```
## Using the app.
The app can be accessed via a **POST** request.
```bash
curl -X POST http://localhost:8000/api/locations/Athens/?days=7
# sample response
{"maximum":"36.50","minimum":"21.40","average":"28.84","median":"27.80"}
```
## Running tests
### On docker
1. Run the app
   ```bash
   docker-compose up
   ```
2. On a separate terminal window, navigate to the repository and get the name of the weather app's container
   ```bash
   docker-compose ps

   Name                     Command               State           Ports
   -----------------------------------------------------------------------------------
   weather_weather_1   python manage.py runserver ...   Up      0.0.0.0:8000->8000/tcp
   ```
3. Execute the tests
   ```bash
   docker exec -it weather_weather_1 coverage run manage.py test api/tests/
   ```
4. To view test coverage, run the following command
    ```bash
   docker exec -it weather_weather_1 coverage report -m
   ```

### On bare-metal
1. Run the tests
   ```bash
   coverage run manage.py test api/tests/
   ```
4. To view test coverage, run the following command
    ```bash
   coverage report -m
   ```

## Viewing logs
Logs can be viewed as follows.
### On docker
```bash
docker logs weather_weather_1
```

### On bare-metal
Logs can be viewed inside the `weather.log` file inside the parent folder.
