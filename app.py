from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
# A secret key is required to use sessions
app.secret_key = 'your_very_secret_key_here' # Replace with a real secret key

# In-memory "database" to store user submissions for the dashboard
users_db = []

# Home page route (form)
@app.route('/')
def home():
    return render_template('index.html')

# Form submission route
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    password = request.form.get('password')

    # Basic server-side validation
    if not name or not email or not password:
        # In a real app, you might flash a message and re-render the form
        # For this example, we'll just redirect home.
        return redirect(url_for('home'))
    
    # Add user to our in-memory list
    users_db.append({'name': name, 'email': email})
    
    # Store user's name in the session
    session['user'] = name

    # Redirect to the success page
    return redirect(url_for('success'))

# Dashboard route
@app.route('/dashboard')
def dashboard():
    user_count = len(users_db)
    return render_template('dashboard.html', users=users_db, user_count=user_count)

# Success route to show confirmation
@app.route('/success')
def success():
    user = session.pop('user', 'Guest') # Get user from session, with a default
    return render_template('success.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
