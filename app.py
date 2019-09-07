from flask import Flask
app = Flask(__name__)

@app.route('/<destination>')
def api(destination):
	return f'You\'re destination is: {destination}'

@app.route('/suck')
def suck():
	return 'suck my dick'

if __name__ == '__main__':
	app.run()