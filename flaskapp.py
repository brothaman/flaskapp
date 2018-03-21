#!/usr/bin/env python

import os
import flask
import urllib2

template_dir = os.path.abspath('/var/www/html/flaskapp/templates')
# Create the application.
#app = flask.Flask(__name__, template_folder=template_dir)
app = flask.Flask(__name__)

@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    response1 = urllib2.urlopen('http://169.254.169.254/latest/meta-data/instance-id')
    response2 = urllib2.urlopen('http://169.254.169.254/latest/meta-data/ami-launch-index')
    response3 = urllib2.urlopen('http://169.254.169.254/latest/meta-data/public-hostname')
    response4 = urllib2.urlopen('http://169.254.169.254/latest/meta-data/public-ipv4')
    response5 = urllib2.urlopen('http://169.254.169.254/latest/meta-data/local-hostname')
    response6 = urllib2.urlopen('http://169.254.169.254/latest/meta-data/local-ipv4')

    html1 = response1.read()
    html2 = response2.read()
    html3 = response3.read()
    html4 = response4.read()
    html5 = response5.read()
    html6 = response6.read()
    return flask.render_template('index.html', html1=html1, html2=html2, html3=html3, html4=html4, html5=html5, html6=html6)
#    return html4


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')
