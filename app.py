import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, g, jsonify

app = Flask(__name__)


app.secret_key = 'ma_cle_secrete_super_dangereuse'

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],))
    user = cur.fetchone()
    
    return render_template('index.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        cur = db.cursor()
        
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        print(f"DEBUG - Requête exécutée : {query}") 
        
        try:
            cur.execute(query) 
            user = cur.fetchone()

            if user:
                session['user_id'] = user['id']
                session['username'] = user['username']
                return redirect(url_for('index'))
            else:
                error = "Identifiants invalides."
        except Exception as e:
            error = f"Erreur SQL : {e}"

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cur = db.cursor()
        
        try:
            cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
            db.commit()
            return redirect(url_for('login'))
        except Exception as e:
            return f"Erreur : {e}"
            
    return render_template('register.html')

@app.route('/leaderboard')
def leaderboard():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT username, score FROM users ORDER BY score DESC LIMIT 10")
    users = cur.fetchall()
    return render_template('leaderboard.html', users=users)


@app.route('/update_score', methods=['POST'])
def update_score():
    if 'user_id' not in session:
        return jsonify({'error': 'Non connecté'}), 403

    data = request.get_json()
    new_score = data.get('score')

    db = get_db()
    cur = db.cursor()
    cur.execute("UPDATE users SET score = ? WHERE id = ?", (new_score, session['user_id']))
    db.commit()

    return jsonify({'status': 'success', 'new_score': new_score})

if __name__ == '__main__':
    app.run(debug=True)