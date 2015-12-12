#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()

def htmlTop():
    print '''<!DOCTYPE html>
            <html lang="en-us">
            <head>
                <meta charset="UTF-8">
                <title>PianoSongGenerator by mattbat131</title>
            </head>
            <body>'''

def htmlBot():
    print '''</body>
            </html>'''


def getData():
    formData = cgi.FieldStorage()
    rating = formData.getvalue('rating')
    return rating

print "Content-type: text/html"
print
htmlTop()
rate = getData()
print "you rated {0}".format(rate)
htmlBot()
