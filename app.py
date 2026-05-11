''' Gender 1 Female 0 Male
    churn 1 Yes 0 NO
    Scaler is exported as scalar.pkl
    Model is exported as model.pkl
    Order of the X Age,Gender,Tenure,MonthlyChargers
'''

import streamlit as st
import joblib
import numpy as np

scaler=joblib.load("scaler.pkl")
model=joblib.load("model.pkl")

st.title("Customer Churn Prediction")

st.divider()

st.write("Please enter the following details and press the predict button for the prediction")

st.divider()

age=st.number_input("Enter Age",min_value=18,max_value=100,value=25)

tenure=st.number_input("Enter Tenure",min_value=0,max_value=130,value=10)

monthlyCharge=st.number_input("Enter Monthly Charge",min_value=30,max_value=150)

gender=st.selectbox("Enter Gender",["Female","Male"])

st.divider()

predictbutton=st.button("Predict")
st.divider()

if predictbutton:

    gender_selected=1 if gender=="Female" else 0
    
    X=[age,gender_selected,tenure,monthlyCharge]
    
    X1=np.array(X)
    
    X_array=scaler.transform([X1])
    prediction=model.predict(X_array)[0]
    
    prediction="Churn" if prediction==1 else "Not Churn"
    
    st.balloons()
    
    st.write(f"The customer is likely to {prediction}")

else:
    st.write("Please Enter all the details and click the predict button to see the result")


    
    
