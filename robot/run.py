# -*- coding: utf-8 -*-
from eve import Eve

app = Eve()

@app.route('/rest/mars/<cmd>', methods=['GET','POST'])
def appRestMarsJson(cmd):
	from robot import Robot
	return Robot(cmd).getLocation()

@app.route('/text/mars/<cmd>', methods=['GET','POST'])
def appRestMarsText(cmd):
	from robot import Robot
	return Robot(cmd).getLocationText()

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)
