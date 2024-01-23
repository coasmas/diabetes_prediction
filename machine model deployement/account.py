# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:30:36 2024

@author: cosma
"""

import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth

# we are linking our application with the firebase database
cred=credentials.Certificate('F:\machine model deployement\diabetic-check-f3dca2f0a1e3.json')
#firebase_admin.initialize_app(cred)

def app():
    #Usernm=[]
    #st.header('Welcome to our :orange[Diabetic app checker]')
    #choice= st.selectbox('Login/Signup', ['Login', 'Sign Up'])
    
    if 'username' not in st.session_state:
        st.session_state.username=''
    
    if 'useremail' not in st.session_state:
        st.session_state.useremail=''
    
    
    def f():
            try:
                user=auth.get_user_by_email(email)
                #print(user.uid)#before it is a comment
                
                
                
                st.write('Login Successful')
                
                st.session_state.username=user.uid
                st.session_state.useremail=user.email
                
           
                global Usernm
                Usernm=(user.uid)
                st.session_state.signedout = True
                st.session_state.signout = True  
                
            except:
                st.warning('Login Failed', icon="🛠")
                
    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''
        
                
    if 'signedout' not in st.session_state:
        st.session_state.signedout= False
        
    if 'signout' not in st.session_state:
        st.session_state.signout= False
        
    if not st.session_state['signedout']:
        choice= st.selectbox('Login/Signup', ['Login', 'Sign Up'])
        
        if choice=='Login':
            email= st.text_input('Email-Address')
            password= st.text_input('Password', type='password')
            
            st.button('Login', on_click=f)
            
            
        
        else:
            email= st.text_input('Email-Address')
            password= st.text_input('Password', type='password')
            
            username= st.text_input('Enter your unique username')
            
            if st.button('Create my account'):
               user = auth.create_user(email = email, password = password, uid=username)
               
               st.success('Account created successfully')
               st.markdown('Please Login using your email and password')
               st.balloons()
    
    if st.session_state.signout:
        st.text('Name '+st.session_state.username)
        st.text('Email id: '+st.session_state.useremail)
        st.button('Sign out', on_click=t) 
            
                
    

                            
    def app():
        st.write('Posts')
           
            
        