from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory user data
users = []

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        balance = request.form['balance']
        users.append({
            'full_name': full_name,
            'email': email,
            'balance': balance
        })
        return redirect('/')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
