import streamlit as st
import requests

st.title("🌸 Iris Prediction")

st.write("Enter the feature values below:")

# User input fields
sepal_length = st.number_input("Sepal Length", value=5.1)
sepal_width = st.number_input("Sepal Width", value=3.5)
petal_length = st.number_input("Petal Length", value=1.4)
petal_width = st.number_input("Petal Width", value=0.2)

# Button
if st.button("Predict"):
    api_url = "http://127.0.0.1:8000/predict"  # Your FastAPI URL
    
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    # Send request to FastAPI
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"🌼 Predicted Class: **{prediction}**")
    else:
        st.error("❌ Error: Could not get response from API")
