# Gender
# Married
# Dependents
# Education
# Self_Employed
# ApplicantIncome
# CoapplicantIncome
# LoanAmount
# Loan_Amount_Term
# Credit_History
# Property_Area

import pickle
import streamlit as st

# loading the saved models
loan_model = pickle.load(open('loan_model.sav', 'rb'))

#page title
st.title('oan Status Prediction Using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Gender = st.text_input("Select 1 for Male and 0 for female")
with col2:
    Married = st.text_input("Select 1 for Married 0 for Unmarried")
with col3:
    Dependants  = st.text_input("Enter number of Dependants")

with col1:
    Education  = st.text_input("Select 1 for Graduate 0 for Under Graduate")
with col2:
    Self_Employed  = st.text_input("Select 1 for Yes 0 for No")
with col3:
    ApplicantIncome  = st.text_input("Enter Applicants Income")

with col1:
    CoapplicantIncome  = st.text_input("Enter Coapplicants Income")
with col2:
    LoanAmount  = st.text_input("Enter Loan Amount")
with col3:
    Loan_Amount_Term  = st.text_input("Enter Loan amount term")

with col1:
    Credit_History  = st.text_input("Select 1.0 for Credit 0 for remaining")
with col2:
    Property_Area  = st.text_input("Select 2 for Urban 0 for Rural")

#code for Prediction
loan_pred = ''

#creating a button for prediction
if st.button('Loan Status'):
    loan_prediction = loan_model.predict([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])

    if(loan_prediction[0]==1):
        loan_pred='Yes'
    else:
        loan_pred='No'
st.success(loan_pred)