from flask import Flask, redirect, render_template, request

app = Flask(__name__)
#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#app.config['SERVER_NAME'] = 'hiredhalal.com'

@app.route('/')
def index():
    print("Hello Mars")
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)
