import pickle
import streamlit as st
model1=pickle.load(open("insurance.pkl","rb"))

def mydeploy():
    st.title("insurance prediction")
    age=st.number_input("enter your age")
    pred=st.button("predict")

    if pred:
        x=model1.predict([[age]])
        result = {0: "No", 1: "Yes"}
        st.write("insurance is : ", result.get(x[0], "Unknown"))
         
mydeploy()
    
