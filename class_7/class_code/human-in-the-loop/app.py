import uuid
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests
import json

API_URL = "http://localhost:8001"

st.set_page_config(
    page_title="Customer Service AI Assistant",
    page_icon="🤖",
    layout="wide"
)

def generate_service_plan(customer_message: str) -> dict:
    """Call the API to generate a service plan"""
    response = requests.post(
        f"{API_URL}/generate-plan",
        json={"message": customer_message}
    )
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error generating plan: {response.text}")
        return None

def save_feedback_to_dataset(run_id: str, customer_message: str, corrected_plan: str):
    """Call the API to save feedback"""
    response = requests.post(
        f"{API_URL}/save-feedback",
        json={
            "run_id": run_id,
            "customer_message": customer_message,
            "corrected_plan": corrected_plan
        }
    )
    if response.status_code != 200:
        st.error(f"Error saving feedback: {response.text}")

def main():
    st.title("🤖 Customer Service AI Assistant")
    st.markdown("""
    This AI assistant helps generate step-by-step plans for customer service inquiries.
    Enter the customer's message below to get started.
    """)

    # Session state initialization
    if 'current_plan' not in st.session_state:
        st.session_state.current_plan = None
    if 'run_id' not in st.session_state:
        st.session_state.run_id = None

    # Customer message input
    customer_message = st.text_area(
        "Customer Message",
        height=150,
        placeholder="Enter the customer's message here..."
    )

    # Generate button
    if st.button("Generate Service Plan", type="primary"):
        with st.spinner("Generating service plan..."):
            result = generate_service_plan(customer_message)
            if result:
                st.session_state.current_plan = result["service_plan"]
                st.session_state.run_id = str(uuid.uuid4())

    # Display results and feedback section
    if st.session_state.current_plan:
        st.subheader("Generated Service Plan")
        st.write(st.session_state.current_plan)

        # Feedback section
        st.divider()
        st.subheader("Feedback Section")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Was this plan helpful?")
            if st.button("👍 Yes"):
                if st.session_state.run_id:
                    save_feedback_to_dataset(
                        st.session_state.run_id,
                        customer_message,
                        st.session_state.current_plan
                    )
                st.success("Thank you for your feedback!")

        with col2:
            st.markdown("### Submit Corrected Plan")
            corrected_plan = st.text_area(
                "Enter corrected version if needed",
                value=st.session_state.current_plan,
                height=200
            )
            if st.button("Submit Correction"):
                if st.session_state.run_id:
                    save_feedback_to_dataset(
                        st.session_state.run_id,
                        customer_message,
                        corrected_plan
                    )
                st.success("Thank you for your correction!")

    # Add some styling
    st.markdown("""
    <style>
    .stButton button {
        width: 100%;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 