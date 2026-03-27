from flask import Flask, render_template, request
from markupsafe import escape # Import escape to prevent XSS attacks


app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    name = request.form['name']
    return render_template('form.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)