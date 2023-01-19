from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']

    with open('database.csv', 'a', newline="") as db:
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)

        return redirect('/thankyou')
    else:
        return 'mistakes were made'


@app.route("/<string:page>")
def page(page):
    print(page + '.html')
    return render_template(page + '.html')



        