from flask import Flask, render_template, jsonify
from pomodoro import Pomodoro, app, pomodoro_obj


# Existing code
# ...

@app.route("/")
def home():
    # Render the home.html template and pass the pomodoro object as a JSON object
    return render_template("home.html", pomodoro=pomodoro_obj.to_json())

# Define a route for the start_pomodoro function
@app.route("/start_pomodoro")
def start_pomodoro():
    # Existing code
    # ...
    # Return a JSON object with the pomodoro object and a success message
    return jsonify({
        "pomodoro": pomodoro_obj.to_json(),
        "message": "Pomodoro started!"
    })

# Define a route for the add_five_minutes function
@app.route("/add_five_minutes")
def add_five_minutes():
    # Existing code
    # ...
    # Return a JSON object with the pomodoro object and a success message
    return jsonify({
        "pomodoro": pomodoro_obj.to_json(),
        "message": "Five minutes added!"
    })

# Define a route for the skip_to_break function
@app.route("/skip_to_break")
def skip_to_break():
    # Existing code
    # ...
    # Return a JSON object with the pomodoro object and a success message
    return jsonify({
        "pomodoro": pomodoro_obj.to_json(),
        "message": "Skipped to break!"
    })

# Define a route for the skip_to_study function
@app.route("/skip_to_study")
def skip_to_study():
    # Existing code
    # ...
    # Return a JSON object with the pomodoro object and a success message
    return jsonify({
        "pomodoro": pomodoro_obj.to_json(),
        "message": "Skipped to study!"
    })
