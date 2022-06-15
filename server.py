# to activate:
# <venv>\Scripts\Activate.ps1
# $env:FLASK_APP="server.py"
# $env:FLASK_ENV="development"
# flask run
# deactivate

# import email
# from email import message
# from inspect import ?????
from flask import Flask, render_template, url_for, request, redirect
from flask import request
import csv

app = Flask(__name__)  # this is our flask app

print(__name__)  # is equal __main__


# higher level of abstraction, anything we click / define the function


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# to store data that we grab with the form:


def write_to_file(data):
    with open('database.txt', mode='a') as database:  # mode a append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

# with module csv


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:  # mode a append
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

# from flask request object


# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         # print(data)
#         # write_to_file(data)
#         write_to_csv(data)
#         return redirect('thankyou.html')
#         return 'did not save to database'
#     else:
#         return 'something went wrong. Try again!'

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

# to have a thank you page we copy contactt html with thankyou.html
