# isthejmzrunning

What's up with the J/M/Z trains? This app will tell you right quick.

## Start the app

``` sh
export PRODUCTION=False DEV_CONFIG=./dev_config.cfg
flask run
```

Locally, this app runs on `localhost:5000`.

In production, this app runs on a Gunicorn server, which can also be used locally:

``` sh
export PRODUCTION=False DEV_CONFIG=./dev_config.cfg
gunicorn isthejmzrunning.isthejmzrunning:app -b 0.0.0.0:8000
```

In this example, the app would run on `localhost:8000`.

## To-do
- add logging... for now, just using print()

## Resources
http://datamine.mta.info/list-of-feeds

http://datamine.mta.info/sites/all/files/pdfs/GTFS-Realtime-NYC-Subway%20version%201%20dated%207%20Sep.pdf

https://developers.google.com/transit/gtfs-realtime/

## Notes
Following deployment instructions from https://medium.com/the-andela-way/deploying-your-flask-application-to-heroku-c99050bce8f9