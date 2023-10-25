from flask import Flask, render_template, request
import Jetson.GPIO as GPIO

app = Flask(__name__)

# Pin Definitions (Modify these according to your setup)
relay_pins = [7, 7,7,7,7]  # Pins for Relays

# Set up the GPIO channels
GPIO.setmode(GPIO.BOARD)
for pin in relay_pins:
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)  # Relay pins setup, initial LOW (OFF)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/toggle", methods=["GET"])
def toggle_relay():
    relay_number = int(request.args.get("relay"))
    GPIO.output(relay_pins[relay_number], not GPIO.input(relay_pins[relay_number]))
    return "Relay {} toggled!".format(relay_number)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

