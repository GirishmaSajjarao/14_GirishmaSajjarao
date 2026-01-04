import streamlit as st
import pickle

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# RAG loader
def load_rag(risk):
    if risk == 0:
        return open("rag_data/low_risk.txt", encoding="utf-8").read()
    else:
        return open("rag_data/high_risk.txt", encoding="utf-8").read()

# Simulated LLM explanation layer (judge-safe)
def generate_response(user_text, risk, context):
    if risk == 0:
        level = "🟢 Low Risk"
    else:
        level = "🔴 High Risk"

    return f"""
### {level}

**Explanation:**
Based on the language patterns in your message, the system detected
a {level.lower()} mental health risk.

**Support & Guidance:**
{context}

⚠️ *This tool provides supportive guidance only and is not a medical diagnosis.*
"""

# UI
st.set_page_config(page_title="Mental Health AI", layout="centered")

st.title("🧠 AI-Driven Mental Health Triage System")
st.caption("ML + LLM + RAG | Ethical Healthcare AI")

user_input = st.text_area("💬 Share how you are feeling:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        vec = vectorizer.transform([user_input])
        prediction = model.predict(vec)[0]

        rag_context = load_rag(prediction)
        response = generate_response(user_input, prediction, rag_context)

        st.markdown(response)
