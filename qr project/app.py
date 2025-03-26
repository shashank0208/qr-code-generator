from flask import Flask, render_template, request
import qrgenerator  # Import the QR code generator function

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    url = request.form.get("url")  # Get URL input from form

    qr_path = qrgenerator.generate_qr(url)  # Generate QR code and get file path

    return render_template("index.html", qr_image=qr_path)  # Pass the QR code path to the template

if __name__ == "__main__":
    app.run(debug=True)
