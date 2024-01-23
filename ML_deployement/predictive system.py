# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# loading the save model 'rb' means reading the binary format
loaded_model =pickle.load(open('F:/machine model deployement/Trained_model.sav','rb')) 
input_data=()

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
  print('The person is not Diabetic')

else:
  print('The person is Diabetic')


