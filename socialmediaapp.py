from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample database representation
users = {
    'user1': {'username': 'user1', 'password': 'password1', 'posts': []},
    'user2': {'username': 'user2', 'password': 'password2', 'posts': []}
}

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    users[username] = {'username': username, 'password': password, 'posts': []}
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username not in users or users[username]['password'] != password:
        return jsonify({'message': 'Invalid credentials'}), 401
    return jsonify({'message': 'Login successful'}), 200

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    username = data['username']
    post_content = data['content']
    if username not in users:
        return jsonify({'message': 'User not found'}), 404
    users[username]['posts'].append(post_content)
    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/timeline/<username>', methods=['GET'])
def timeline(username):
    if username not in users:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'timeline': users[username]['posts']}), 200

if __name__ == '__main__':
    app.run(debug=True)
