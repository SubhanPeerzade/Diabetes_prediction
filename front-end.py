import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('E:/Pycharm Programs/flaskApp/new_trained_model.sav', 'rb'))

#creating a function for prediction

def diabetes_prediction (input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return ('The person is not diabetic')
    else:
        return ('The person is diabetic')

def main():

    # Giving a title
    st.title('Diabetes Prediction Web App')

    # Getting the input data from user

    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Number of Glucose level")
    BloodPressure = st.text_input("Number of Blood Pressure value")
    SkinThickness = st.text_input("Number of Skin Thickness value")
    Insulin = st.text_input("Number of Insulin Level")
    BMI = st.text_input("Number of BMI")
    DiabetesPedigreeFunction = st.text_input("Number of Diabetes Pedigree Function")
    Age = st.text_input("Age value")

    # code for Prediction

    diagnosis = ''

    # Creating a button for prediction

    if st.button('Diabetes Test Resut'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()
