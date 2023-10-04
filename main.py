from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_

app = Flask(__name__)
app.secret_key = 'dnyaneshyeole'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/irctc'
db = SQLAlchemy(app)


class Train(db.Model):
    train_number = db.Column(db.Integer, primary_key=True)
    train_name = db.Column(db.String(100))
    source = db.Column(db.String(50))
    destination = db.Column(db.String(50))
    distance = db.Column(db.Integer)
    total_time = db.Column(db.String(50))
    departure = db.Column(db.String(50))
    arrival = db.Column(db.String(50))


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    train_number = db.Column(db.Integer)
    train_name = db.Column(db.String(100))
    station_name = db.Column(db.String(100))
    station_code = db.Column(db.String(10))
    day = db.Column(db.String(10))
    arrival = db.Column(db.String(10))
    departure = db.Column(db.String(10))

@app.route('/')
def home():
    return render_template('home.html')


# Route for displaying the login form
@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')


# Route for handling the login form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password match a user in the database
    user = Users.query.filter_by(username=username, password=password).first()

    if user:
        flash('Login successful!', 'success')
        # You can redirect the user to a different page after successful login
        return redirect('/search_train')
    else:
        flash('Invalid username or password', 'error')
        return redirect('/login')

# Route for displaying the signup form
@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

# Route for handling the signup form submission
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username is already taken
    existing_user = Users.query.filter_by(username=username).first()
    if existing_user:
        flash('Username already taken', 'error')
        return redirect('/signup')

    # Create a new user and add it to the database
    new_user = Users(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    flash('Sign up successful!', 'success')
    return redirect('/login')



@app.route('/search_train')
def index():
    return render_template('search_train.html')

@app.route('/search', methods=['POST'])
def search():
    source = request.form.get('source')
    destination = request.form.get('destination')

    trains = Train.query.filter(and_(Train.source.ilike(f'%{source}%'), Train.destination.ilike(f'%{destination}%'))).all()

    return render_template('search_results.html', source=source, destination=destination, trains=trains)


@app.route('/add_train', methods=['GET', 'POST'])
def add_train():
    if request.method == 'POST':
        train_name = request.form.get('train_name')
        train_number = request.form.get('train_number')
        source = request.form.get('source')
        destination = request.form.get('destination')
        distance = request.form.get('distance')
        total_time = request.form.get('total_time')
        departure = request.form.get('departure')
        arrival = request.form.get('arrival')
        train = Train(
            train_number=train_number,
            train_name=train_name,
            source=source,
            destination=destination,
            distance=distance,
            total_time=total_time,
            departure=departure,
            arrival=arrival
        )
        db.session.add(train)
        db.session.commit()
        return redirect('/')
    return render_template('add_train.html')


# Route for displaying the train schedule search form
@app.route('/schedule', methods=['GET'])
def schedule_form():
    return render_template('schedule.html')

# Route for handling the train schedule search form submission
@app.route('/schedule', methods=['POST'])
def schedule():
    train_input = request.form.get('train_input')

    # Query the schedule table for the given train input
    schedules = Schedule.query.filter(or_(Schedule.train_name.ilike(f'%{train_input}%'), Schedule.train_number == train_input)).all()

    return render_template('schedule_results.html', train_input=train_input, schedules=schedules)


@app.route('/about')
def about():
    return render_template('about.html')

# project completed

if __name__ == '__main__':
    app.run(debug=True)
