from flask import Flask, render_template
from db import fetch

feed_data=fetch()
id=[]
feedback=[]
for i in feed_data:
	id.append(int(i.get('id')))
	feedback.append(i.get('feedback'))

app=Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/apps/<string:id>/')
def apps(id):
	return render_template('app.html',feedback=feedback,id=id)





if __name__ == '__main__':
	app.run(debug="true")


# {%includes  %} for including files
#use {% %} for logic
#use {} for variables