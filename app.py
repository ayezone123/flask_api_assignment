from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data
profiles = []
routines = {
    "dry": ["Gentle cleanser", "Hydrating toner", "Heavy moisturizer", "SPF 30+"],
    "oily": ["Foaming cleanser", "Exfoliating toner", "Light moisturizer", "Oil-free SPF"],
    "combination": ["Balancing cleanser", "Toner", "Gel moisturizer", "SPF"],
    "sensitive": ["Fragrance-free cleanser", "Soothing toner", "Barrier-repair cream", "Mineral SPF"]
}
wellness_logs = []

# POST: Add profile
@app.route('/profiles', methods=['POST'])
def add_profile():
    data = request.get_json()
    profiles.append(data)
    return jsonify({"message": "Profile added", "profile": data}), 201

# GET: Get routine by skin type
@app.route('/routine/<skin_type>', methods=['GET'])
def get_routine(skin_type):
    routine = routines.get(skin_type.lower())
    if routine:
        return jsonify({"skin_type": skin_type, "routine": routine})
    else:
        return jsonify({"message": "No routine found"}), 404

# POST: Log wellness data
@app.route('/wellness', methods=['POST'])
def log_wellness():
    data = request.get_json()
    wellness_logs.append(data)
    return jsonify({"message": "Wellness data logged", "entry": data}), 201

# GET: View wellness logs
@app.route('/wellness', methods=['GET'])
def view_wellness():
    return jsonify(wellness_logs)

if __name__ == '__main__':
    app.run(debug=True)
