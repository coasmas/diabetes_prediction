# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:13:42 2023

@author: cosma
"""

import numpy as np 
#import matplotlib.pyplot as plt
import pickle
import streamlit as st # this library is used for creating the web page
from streamlit_option_menu import option_menu
#import json
#from streamlit_lottie import st_lottie
import pandas as pd
from firebase_admin import firestore
#import streamlit_authenticator as stauth

import account


#diabetes_df = pd.read_csv('diabetes.csv')
#loading dataset from csv file to pandas dataframe)
diabetes_file_path='F:\machine model deployement/diabetes.csv'
diabetes_df=pd.read_csv(diabetes_file_path)

    
page_title="Diabete Web App Checker"
page_icon= ":medical_symbol:"
layout="centered" #"wide"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title +""+ page_icon)



page_bg_img=f"""
<style>
[data-testid="stAppViewContainer"] > .main{{
    background-image:linear-gradient(rgba(0, 0, 0, 0.527),rgba(0, 0, 0, 0.5)) , url("https://img.freepik.com/premium-photo/doctor-holding-stethoscope-hospital-blur-blue-background_103324-537.jpg?w=740");
    background-size: cover; 
    background-position:center top ;
    background-repeat: no-repeat;
    background attachement: local;
    }}

[data-testid="stMarkdownContainer"]{{
    color:white;
    }} 
[id="47786f7"]{{
    color:darkblue;
    }} 
[id="abstract"]{{
    color:darkblue;
    }} 
[id="introduction"]{{
    color:darkblue;
    }} 
[id="application-of-machine-learning-in-healthcare"]{{
    color:darkblue;
    }} 
[data-testid="baseButton-secondary"]{{
    background-color:orange;
    }}
[data-testid="element-container"]{{
    color:orange;
    }}
[data-testid="stHeader"]{{
    background-color: rgba(0, 0, 0, 0);
    }}

[data-testid="element-container"]{{
    right: 1rem;
    }}
</style>
"""
st.markdown(page_bg_img ,unsafe_allow_html=True)

# loading the save model 'rb' means reading the binary format
loaded_model =pickle.load(open('F:/machine model deployement/Trained_model.sav','rb')) 
# 20 as an Horinzontal bar

#st.title(page_title)
selected = option_menu(
    menu_title=None,#"Main menu", #or None,#required
    options=["Log/sign","Home", "Data Entry"],#required
    icons=["person-circle","house", "hand-index-thumb"], #optional
    menu_icon="cast", #optional
    default_index=0, 
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "#0b1647", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "orange"},
            },
    )

if selected == "Log/sign":
    account.app() 
    
if selected == "Home":
    
    #ph = ''
    if st.session_state.username=='':
        st.write('Login to be able access the system')
    else:
            with st.container():
                st.header("Abstract")
                st.markdown(
                    "Diabetes has emerged as a signifcant global health concern, contributing to various severe complications such as kidney disease, vision loss, and coronary issues. Leveraging machine learning algorithms in medical services has shown promise in accurate disease diagnosis and treatment, thereby alleviating the burden on healthcare professionals. The feld of diabetes forecasting has rapidly evolved, ofering the potential for early intervention and patient empowerment."
                    )
                                    #plt.figure(figsize=(12,10))
                                    # seaborn has an easy method to showcase heatmap
                                    #p = sns.heatmap(diabetes_df.corr(), annot=True,cmap ='RdYlGn')
                st.line_chart(diabetes_df)
            with st.container():
                st.header("Introduction") 
                st.markdown("""Diabetes is a persistent condition described by a raised blood glucose level. Diabetes
                                        causes moderate kidney, eye, and heart harm after some time [1]. Early detection of diabetes is a difcult task. Diabetes sickness can be categorized into three classes: Type 1
                                        diabetes, also known insulin-dependent diabetes or juvenile diabetes, happens when the
                                        body’s safe framework harms insulin-delivering cells, ending insulin creation [2]. More
                                        than 90% of DM cases are those of type 2 diabetes. As of late, the frequency of type 2
                                        diabetes has been expanding signifcantly every year [3]. As per the most recent overview
                                        delivered by the Global Diabetes League in 2019, diabetes has a commonness of 9.3%, and
                                        it afects roughly 463 million grown-ups around the world. It is normal that the quantity
                                        of afected people will arrive at 578 million (10.2%) by 2030 and 700 million (10.9%)
                                        by 2045 [4]. Diabetes is especially hazardous for pregnant ladies, and unborn youngsters
                                        are probably going to be impacted by this infection. By and large, assuming the glucose
                                        level in the blood transcends the ordinary worth, the individual is viewed as diabetic.
                                        """ )
                st.area_chart(diabetes_df)
                #st.plotly_chart(px.scatter(df, x="sepal_width", y="sepal_length", color="species"))
            with st.container():
                st.header("Application of machine learning in healthcare")
                st.markdown(""""The increasingly growing number of applications of machine learning in healthcare allows
                                        us to glimpse at a future where data, analysis, and innovation work hand-in-hand to help
                                        countless patients without them ever realizing it.
                                        • Identifying Diseases and Diagnosis: One of the main applications of ML in healthcare is the identifcation and diagnosis of diseases and ailments which are otherwise
                                        considered hard-to-diagnose. This can include anything from cancers which are tough
                                        to catch during the initial stages, to other genetic diseases.
                                        • Smart Health Records: The main role of machine learning in healthcare is to ease
                                        processes to save time, efort, and money. Document classifcation methods using vector machines and ML-based OCR recognition techniques are slowly gathering steam,
                                        such as Google’s Cloud Vision API and MATLAB’s machine learning-based handwriting recognition technology."""
                                )

   
#creating a function for prediction
if selected == "Data Entry":
    if st.session_state.username=='':
        st.write('Login to be able access the system')
    else:
        def diabetes_prediction(input_data):
        
            #change the input_data to numpy array
            input_data_as_numpay_array=np.asarray(input_data)
        
            #to reshape the array as we are predicting for one instance
            #reshape ( ) got 2 parameter
            input_data_reshaped= input_data_as_numpay_array.reshape(1,-1)
        
            # standardize the input data
            #std_data = scaler.transform(input_data_reshaped)
            #print(std_data)
        
            prediction= loaded_model.predict(input_data_reshaped)
            print(prediction)
        
            if (prediction[0]==0):
              return'The person is not Diabetic'
        
            else:
              return'The person is Diabetic'
        
        
        def main():
            
            #Web page Title
            #st.title('Web App Sytem made by Cosmas')
            #create now some input data field where user can enter data
            #getting input data from the user using **st.test_input** this will get input from the usre
            Pregnancies = st.text_input('Number of Pregnancies')
            Glucose= st.text_input('Glucose Level')
            BloodPressure= st.text_input('Blood pressure Value')
            SkinThickness= st.text_input('Skin Thickness')
            Insulin= st.text_input('Insulin level')
            BMI= st.text_input('BMI value')
            DiabetesPedigreeFunction= st.text_input(' Diabetes Pedigree Function')
            Age= st.text_input('The Age of the patient')
            
            
            # Code for Prediction
            diagnosis ='' #null string
            
            # Creating a button for prediction submitted data
            
            if st.button('Diabetes test Result'):
                diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
            
            
            st.success(diagnosis)
    
    
        if __name__ == '__main__':
            main()
