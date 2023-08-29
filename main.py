import serial
import requests

# Set the serial port and baud rate for your Arduino
serial_port = 'COM3'  
baud_rate = 9600

# Google Chat Webhook URL 
webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAEjl5kvc/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=_tIeR7xzVQG7L92jkCz17y8_r21kBeVtgWbQIeQJpNk'

# Open the serial connection to the Arduino
ser = serial.Serial(serial_port, baudrate=baud_rate)

while True:
    # Read data from the Arduino
    data = ser.readline().strip().decode('latin-1')

    # Process and prepare the data as needed
    sensor_data = data  # Replace this with your data processing logic

    # Create a JSON payload with the data you want to send to Google Chat
    payload = {"text": f"{sensor_data}"}

    # Send the data to Google Chat via HTTP POST request
    response = requests.post(webhook_url, json=payload)

    print(f"Data sent to Google Chat. Response: {response.status_code}")