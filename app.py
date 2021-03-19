from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SERVER_NAME'] = 'hiredhalal.com'

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
   app.run(host=app.config["SERVER_NAME"],port=443,debug=True)