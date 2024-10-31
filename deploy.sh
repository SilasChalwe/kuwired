#!/bin/bash
# Navigate to your project directory
cd /home/Silas/kuwired

# Pull the latest changes from GitHub
git pull origin main  # Change 'main' to your branch name if needed

# Activate your virtual environment
source /home/Silas/kuwired/venv/bin/activate

# Install any new requirements
pip install -r requirements.txt

# Restart Gunicorn service
sudo systemctl restart kuwired  # Make sure this matches your service name
