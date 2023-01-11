import joblib
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models 

heart_disease_model = joblib.load(open('f.sav','rb'))



# sidebar of the window

title = st.title("")
with st.sidebar:
     selected = option_menu(' Disease Prediction System',
                          
                          [
                           'Heart Disease Prediction'
                           ],
                          icons=['heart'],
                          default_index=0)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        one = st.number_input('st slope flat')
        
    with col2:
        two= st.number_input('st depression')
        
    with col3:
        three = st.number_input('thalassemia reversable defect')
        
    with col1:
        four = st.number_input('resting blood pressure')
        
    with col2:
        five = st.number_input('cholestrol')
        
    with col3:
        six = st.number_input('max heart rate achieved')
        
    with col1:
        seven = st.number_input('sex male')
        
    with col2:
        eight = st.number_input('chest pain type atypical angina')
        
    with col3:
        nine = st.number_input('chest pain type typical angina')
        
    with col1:
        ten = st.number_input('thalassemia normal')
        
    with col2:
        one1 = st.number_input('fasting blood sugar lower')
        
    with col3:
        two1 = st.number_input('rest ecg left ventricular hypertrophy')
        
    
    with col1:
        three1 = st.number_input('rest ecg normal')
        
    with col2:
        four1 = st.number_input('exercise induced angina yes')
        
    with col3:
        five1 = st.number_input('st slope upsloping')
        
    with col1:
        six1 = st.number_input('thalassemia fixed defect')
        
    with col2:
        seven1 = st.number_input('age')
        
    with col3:
        eight1 = st.number_input('num major vessels')
        
    with col1:
        col1 = st.number_input('chest pain type')
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[col1,one,two,three,four,five,six,seven,eight,nine,ten,one1,two1,three1,four1,five1,six1,seven1,eight1]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    