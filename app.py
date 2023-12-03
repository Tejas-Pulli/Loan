import pickle
import streamlit as st
import numpy as np

# loading the saved models
loan_models = pickle.load(open('**/loan_model.sav', 'rb'))

#page title
st.title('Loan Status Prediction Using ML')

# getting the input data from the user

Gender = st.text_input("Gender: Male-1  Female-0")
Married = st.text_input("Marrital Status: Married-1  Unmarried-0")
Dependents  = st.text_input("Enter number of Dependants")
Education  = st.text_input("Education: Graduate-1  Under-Graduate-0")
S_Employed  = st.text_input("Self-Employed: Yes-1  No-0")
ApplicantIncome  = st.text_input("Enter Applicant's Income")
CoapplicantIncome  = st.text_input("Enter Co-applicants Income")
LoanAmount  = st.text_input("Enter Loan Amount")
Loan_Amount_Term  = st.text_input("Enter Loan amount term")
Credit_History  = st.text_input("Credit_History: Yes-1  No-0")
Property_Area  = st.text_input("Property Area: Urban-2 Semiurban-1 Rural-0")

input_data_as_numpy_array = np.array([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

#code for Prediction
loan_pred = ''

#creating a button for prediction
if st.button('Loan Status'):
    loan_prediction = loan_models.predict(input_data_reshaped)
    
    if(loan_prediction[0]==1):
        loan_pred='Cogratulations...! You are eligible for Loan'
    else:
        loan_pred='Sorry...! You are not eligible for Loan'
st.success(loan_pred)
