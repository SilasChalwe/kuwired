from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Verify the request is from GitHub if necessary
    subprocess.call(['bash', 'deploy.sh'])  # Run the deployment script
    return '', 200  # Respond with a 200 status

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on port 5000
