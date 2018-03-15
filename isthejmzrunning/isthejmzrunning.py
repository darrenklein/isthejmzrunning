from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import requests
import env_variables

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('ISTHEJMZRUNNING_SETTINGS', silent=True)

@app.route('/')
def index():
    r = requests.get(f'http://datamine.mta.info/mta_esi.php?key={env_variables.MTA_API_KEY}&feed_id=36')
    print(r.text)
    return render_template('index.html')