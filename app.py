from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def medical_ai(question: str) -> str:
    q = question.lower().strip()

    common_info = (
        "General medical information (educational only):\n"
        "- This does not diagnose or replace a doctor.\n"
    )

    if "paracetamol" in q or "acetaminophen" in q:
        return (
            f"{common_info}\n"
            "Paracetamol (Acetaminophen) is commonly used to reduce fever and relieve mild to moderate pain.\n"
            "Follow the label dosage instructions.\n"
        )
    if "ibuprofen" in q:
        return (
            f"{common_info}\n"
            "Ibuprofen is commonly used for pain, fever, and inflammation.\n"
            "Follow the label dosage instructions.\n"
        )
    if "antibiotic" in q:
        return (
            f"{common_info}\n"
            "Antibiotics treat bacterial infections, not viruses like colds or flu.\n"
            "They should only be used when prescribed by a healthcare professional.\n"
        )
    if "asthma" in q:
        return (
            f"{common_info}\n"
            "Asthma can cause breathing difficulty due to airway inflammation.\n"
            "Common triggers include dust, smoke, exercise, and allergies.\n"
        )

    return (
        f"{common_info}\n"
        f"Question received: {question}\n"
        "This prototype explains basic health topics and common medicines.\n"
    )

def safety_ai(answer: str) -> str:
    safety_notes = (
        "\n\nSafety review (AI supervisor):\n"
        "- If symptoms are severe, worsening, or unusual, seek medical help.\n"
        "- If you are pregnant, have chronic illness, allergies, or take other medicines, ask a doctor/pharmacist.\n"
        "- Follow dosage instructions on the medicine label.\n"
        "⚠️ Disclaimer: Educational information only. Not medical diagnosis.\n"
    )
    return answer + safety_notes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"answer": "Please type a medical question."})

    first_answer = medical_ai(question)
    final_answer = safety_ai(first_answer)
    return jsonify({"answer": final_answer})

if __name__ == "__main__":
    app.run(debug=True)
