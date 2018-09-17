from flask import Flask, render_template
from db import fetch

feed_data=fetch()

app=Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/apps')
def apps():
	return render_template('app.html',feed_data=feed_data)





if __name__ == '__main__':
	app.run(debug="true")


# {%includes  %} for including files
#use {% %} for logic
#use {} for variables