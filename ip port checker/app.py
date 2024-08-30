from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def check_port(ip, port):
    try:
        # Try to establish a socket connection
        sock = socket.create_connection((ip, port), timeout=5)
        sock.close()
        return "Open"
    except (socket.timeout, socket.error):
        return "Closed"

@app.route('/', methods=['GET', 'POST'])
def index():
    status = None
    if request.method == 'POST':
        ip = request.form['ip']
        port = int(request.form['port'])
        status = check_port(ip, port)
    
    return render_template('index.html', status=status)

if __name__ == '__main__':
    app.run(debug=True)
