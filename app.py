import streamlit as st
import requests

# API endpoint
url = "http://127.0.0.1:8000/query"

# Set up the Streamlit app
st.title("Chat Bot")

# Create a form for better user experience
with st.form("chat_form"):
    user_query = st.text_input("Enter your query..")
    submit_button = st.form_submit_button("Submit")

# When the form is submitted
if submit_button:
    if user_query.strip():  # Check if query is not empty
        try:
            # Send POST request with JSON data (more common for chat applications)
            response = requests.post(
                url,
                json={"query": user_query},

            )

            # Check if the request was successful
            response.raise_for_status()

            # Display the response
            # Assuming the response is JSON, adjust if it's plain text
            st.write("Response:")
            st.write(response.json())  # or response.text if not JSON

        except requests.exceptions.RequestException as e:
            st.error(f"Error connecting to the API: {e}")
    else:
        st.warning("Please enter a query.")
