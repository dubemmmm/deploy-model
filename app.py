import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('iris_model.pkl')

# Title of the app
st.title("Iris Species Prediction App")

# Input fields for the features
sepal_length = st.number_input("Enter sepal length (cm)", value=0.0)
sepal_width = st.number_input("Enter sepal width (cm)", value=0.0)
petal_length = st.number_input("Enter petal length (cm)", value=0.0)
petal_width = st.number_input("Enter petal width (cm)", value=0.0)

# Button for making predictions
if st.button("Predict"):
    # Prepare the input data as a numpy array
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make predictions
    prediction = model.predict(input_data)
    species = ['setosa', 'versicolor', 'virginica']

    # Display the prediction
    st.write(f"The model predicts: {species[prediction[0]]}")
