from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')  # Stranger call

@app.route('/ai')
def ai_chat():
    return render_template('ai_call.html')  # AI voice call

@socketio.on('signal')
def handle_signal(data):
    emit('signal', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
