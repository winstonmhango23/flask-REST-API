from flask import Flask

app = Flask(__name__)

@app.route('/students', methods= ["POST","GET"])
def create_student():
  return "This my flask REST API"



if __name__ == '__main__':
    app.run(debug=True)

