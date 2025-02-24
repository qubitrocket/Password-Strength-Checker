from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Password should be at least 12 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if any(not char.isalnum() for char in password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Calculate percentage
    percentage = (strength / 5) * 100

    # Determine strength level
    if strength == 5:
        return "Very Strong", feedback, percentage
    elif strength >= 3:
        return "Strong", feedback, percentage
    elif strength >= 2:
        return "Moderate", feedback, percentage
    else:
        return "Weak", feedback, percentage

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    password = data.get("password", "")
    strength, feedback, percentage = check_password_strength(password)
    return jsonify({"strength": strength, "feedback": feedback, "percentage": percentage})

if __name__ == "__main__":
    app.run(debug=True)