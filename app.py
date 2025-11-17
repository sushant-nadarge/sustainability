import streamlit as st
import pickle
import numpy as np

with open('lrmodel_sustainabel.pkl', 'rb') as file:
    model = pickle.load(file)   
    
st.title =("stataniability prediction")
    
carbon_emission = st.number_input("Carbon Emission",min_value=0.0,format="%f" )
energy_output = st.number_input("Energy Consumption",min_value=0.0,format="%f" )
renewability_index = st.number_input("Renewability Index",min_value=0.0,format="%f" )
cost_efficiency = st.number_input("Cost Efficiency",min_value=0.0,format="%f" )   
    
if st.button("Predict"):
    input_data = np.array([[carbon_emission, energy_output, renewability_index, cost_efficiency]])
    prediction = model.predict(input_data)
        
    if prediction[0] == 1:
        st.success("The energy source is Sustainable")
    else:
        st.info("The energy source is Not Sustainable, Need to Improve")