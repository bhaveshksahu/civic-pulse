import streamlit as st
st.title("Civic Pulse AI")
st.success("The backend is running perfectly!")
from flask import Flask, render_template, request, jsonify
from gemini_classifier import classify_issue
import uuid, json, os
from datetime import datetime

# Automatically looks in the 'templates' folder now!
app = Flask(__name__)
COMPLAINTS_FILE = "complaints.json"

def load_complaints():
    if os.path.exists(COMPLAINTS_FILE):
        with open(COMPLAINTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_complaint(data):
    complaints = load_complaints()
    complaints.append(data)
    with open(COMPLAINTS_FILE, "w") as f:
        json.dump(complaints, f, indent=2)

@app.route("/")
def index():
    return render_template("slide.html")

@app.route("/classify", methods=["POST"])
def classify():
    problem = request.json.get("problem", "")
    try:
        category = classify_issue(problem)
        return jsonify({"category": category})
    except Exception as e:
        return jsonify({"category": "General Support"}), 500

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    problem = data.get("problem", "")
    category = data.get("category", "")
    
    # Automatically route via Groq AI if they picked the Quick Route
    if category in ["AI Route", "Smart Route"]:
        try:
            category = classify_issue(problem)
        except Exception:
            category = "General Support"

    complaint = {
        "id": f"CP-{str(uuid.uuid4().int)[:4]}",
        "location": data.get("location", "Unknown"),
        "problem": problem,
        "category": category, 
        "timestamp": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "user": "ANONYMOUS"
    }
    save_complaint(complaint)
    
    # Return the AI-generated category and ID back to the frontend
    return jsonify({"status": "ok", "id": complaint["id"], "category": complaint["category"]})

@app.route("/complaints", methods=["GET"])
def get_complaints():
    complaints = load_complaints()
    complaints.reverse()
    return jsonify(complaints)
import streamlit.components.v1 as components

# This opens your HTML file and displays it inside the Streamlit app
try:
    with open("templates/slide.html", "r", encoding="utf-8") as f:
        html_data = f.read()
        components.html(html_data, height=1000, scrolling=True)
except Exception as e:
    st.error(f"Could not load UI: {e}")
#if __name__ == "__main__":
 #   app.run(debug=True)
# Place this after your components.html code
st.write("---")
st.subheader("Submit your Evidence")
uploaded_file = st.file_uploader("Upload a photo of the issue", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # This is where your backend logic from gemini_classifier comes in
    st.info("Processing image with AI...")
    # example: result = classify_issue(uploaded_file)
    st.success("Image received! Our team is on the way.")
