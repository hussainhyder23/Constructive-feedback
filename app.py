from flask import Flask , render_templates
from data import articles

app=Flask(__name__)


Feed=Feedback()

@app.route('/')
def index():
	return render_templates("index.html")


@app.route('/app')
def app():
	return render_templates("app.html",feed=Feed)


@app.route('/app/<string:id>')
def app(id):
	return render_templates("app.html",id=id)












if __name__ == '__main__':
	app.run(debug='true')


# {%includes  %} for including files
#use {% %} for logic
#use {} for variables