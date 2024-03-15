from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    dob DATE NOT NULL)''')
    conn.commit()
    conn.close()

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    dob = request.form['dob']
    
    # Client-side validation
    if not name or not email or not age or not dob:
        return jsonify({'error': 'All fields are required'})
    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except ValueError:
        return jsonify({'error': 'Age must be a positive integer'})
    
    # Database interaction
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (name, email, age, dob) VALUES (?, ?, ?, ?)''', (name, email, age, dob))
    conn.commit()
    conn.close()

    return jsonify({'success': 'Data submitted successfully'})

# Route to retrieve data
@app.route('/data')
def get_data():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM users''')
    data = cursor.fetchall()
    conn.close()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
