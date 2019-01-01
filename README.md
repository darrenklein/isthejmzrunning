# isthejmzrunning

In tribute to the beloved https://isthelrunning.com/, here's an app designed to give you a quick update on the general status of the J, M, and Z trains.

## Installation

To install this app's dependencies, run the command

```bash
python setup.py install
```

## Start the app

To run with flask:

```bash
export PRODUCTION=False DEV_CONFIG=./dev_config.cfg FLASK_APP=isthejmzrunning/__init__.py
flask run
```

which will run the app on `localhost:5000`.

In production, this app runs on a Gunicorn server, which can also be used locally:

```bash
export PRODUCTION=False DEV_CONFIG=./dev_config.cfg
gunicorn isthejmzrunning.isthejmzrunning:app -b 0.0.0.0:8000
```

In this example, the app would run on `localhost:8000`.

## Resources

http://datamine.mta.info/list-of-feeds

http://datamine.mta.info/sites/all/files/pdfs/GTFS-Realtime-NYC-Subway%20version%201%20dated%207%20Sep.pdf

https://developers.google.com/transit/gtfs-realtime/

## Notes

Following deployment instructions from https://medium.com/the-andela-way/deploying-your-flask-application-to-heroku-c99050bce8f9

This app's JavaScript has been linted according to ESLint Airbnb base rules: https://www.npmjs.com/package/eslint-config-airbnb-base

## To-do

- add logging... for now, just using print()
- install flask-minify - https://github.com/mrf345/flask_minify/
