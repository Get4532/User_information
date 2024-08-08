from flask import Flask, render_template,jsonify,request
from db_conn.database import add_user_data_db

app = Flask(__name__)

data = {
        'firstName': '***',
        'lastName': '***',
        'mobileno': '***',
        'address': '***',
        'email': '***'
}

@app.route("/")
def user_info():
    return render_template('index.html', form_data = data)

@app.route("/info", methods=['POST'])
def get_info():
    global data
    data = request.form
    add_user_data_db(data)
    return render_template('index.html', form_data = data)

@app.route("/info/JSON", methods=['GET'])
def JSON_data():
    global data
    return jsonify(data)

@app.route("/database")
def remove_row_database():
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)