from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello World!\n'
@app.route('/adeel', methods=['GET'])
def func():
    return "Adeel's Page!\n"
if __name__ == '__main__':
    app.run()
