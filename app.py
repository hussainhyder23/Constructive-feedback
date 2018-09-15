from flask import Flask, render_template

app=Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')







if __name__ == '__main__':
	app.run(debug="true")


# {%includes  %} for including files
#use {% %} for logic
#use {} for variables