import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle as pkl

model= pkl.load(open('insurance_ml.pkl','rb'))


image = Image.open('image.jpg')

st.sidebar.image(image,use_column_width='auto')
st.sidebar.subheader('What is Insurance?')
st.sidebar.markdown('Insurance provides protection in case something unfavourable happens to you. This can be related to medical emergencies, vehicle theft, property damange and even death. It is a written contract between the insurance company and policy holder.')
st.sidebar.markdown('Through this legal contract, the policy holder gets privileges in case of such emergency. As per this agreement, insurer agrees to cover any financial loss for the policy holder. The insurer provides funds based on the loss or risk that is accidental or above the control of the insured')

col1, col2 = st.columns(2)

with col1:
 st.subheader('Health Insurance Premium v1')

 age=st.number_input('Age in Years',step=1,min_value=18)

 sex=st.selectbox('Select Sex',['Male','Female'])
 if sex=='Male':
    sex=1
 else:
    sex=0

 bmi=st.slider('Enter BMI',min_value=16,max_value=55)

 child=st.number_input('Number of children',step=1)

 smoker=st.selectbox('Smoker',['Yes','No'])
 if smoker=='Yes':
    smoker=1
 else:
    smoker=0

 city=st.selectbox('Select city',['Delhi','Mumbai','Chennai','Kolkata'])
 if city=='Delhi':
    c1=1
    c2=0
    c3=0
    c4=0
 elif city=='Mumbai':
    c1=0
    c2=1
    c3=0
    c4=0
 elif city=='Chennai':
    c1=0
    c2=0
    c3=1
    c4=0
 elif city=='Kolkata':
    c1=0
    c2=0
    c3=0
    c4=1

 user_data=[age,sex,bmi,child,smoker,c1,c2,c3,c4]

 if st.button('Show Insurance Premium'):
    pred=model.predict(np.array(user_data).reshape(1,-1))
    st.text('Premium Amount in Rs:')
    st.text(pred[0].round(0))

with col2:
   st.image("https://www.lateet.com/wp-content/uploads/2018/09/types-of-insurance.jpeg")
   st.markdown("Health insurance helps covers routine and emergency medical care costs, often with the option to add vision and dental services separately. In addition to an annual deductible, you may also pay copays and coinsurance, which are your fixed payments or percentage of a covered medical benefit after meeting the deductible. However, many preventive services may be covered for free before these are met.")
