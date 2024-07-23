# import streamlit as st
# import requests


# backend_url = "http://127.0.0.1:8000"

# #set up page config
# st.set_page_config(
#     page_title='Predict Page',
#     layout='wide'
# )


# def show_form():
#     st.title('sepsis prediction app')
  
#     with st.form('input-feature'):
#     # input fields for sepsis features
#         st.header("Input Sepsis Features ")

#         col1, col2 = st.columns(2)

#         with col1:
#             PRG = st.number_input("PRG", min_value=0.0, max_value=50.0, step=0.1, key='prg')
#             PL = st.number_input("PL", min_value=0.0, max_value=300.0, step=0.1, key='pl'  )
#             PR = st.number_input("PR", min_value= 0.0, max_value=200.0, step=0.1, key= 'pr')
#             SK = st.number_input("SK", min_value= 0.0, max_value=200.0, step=0.1, key= 'sk')
#         with col2:
#             TS = st.number_input("TS", min_value= 0.0, max_value=1000.0, step=0.1, key= 'ts')
#             M11 = st.number_input("M11", min_value= 0.0, max_value=100.0, step=0.1, key= 'm11')
#             BD2 = st.number_input("BD2", min_value= 0.0, max_value=10.0, step=0.1, key= 'bd2')
#             Age = st.number_input("Age", min_value= 0.0, max_value=120.0, step=0.1, key= 'age')
#             Insurance = st.number_input("Insurance", min_value= 0.0, max_value=1.0, step=1.0, key= 'insurance')

#          # predict button
#         if st.form_submit_button('Predict Sepsis'):
#             # create dictionary with input data
#             input_data = {
#                 "PRG": PRG,
#                 "PL" : PL,
#                 "PR" : PR,
#                 "SK" : SK,
#                 "TS" : TS,
#                 "M11": M11,
#                 "BD2": BD2,
#                 "Age": Age,
#                 "Insurance": Insurance
#             }

#             #send a request to the FastAPI backend
#             response = requests.post(f"{backend_url}/forest_prediction", json=input_data)

#             # Display the prediction
#             if response.status_code == 200:
#                 prediction = response.json()['prediction']
#                 st.success(prediction)
#             else:
#                 st.error(f"Error: {response.json()['detail']}")

# if __name__== '__main__':
#     show_form()

#backend_url = "http://api-1:80"

# backend_url = "http://127.0.0.1:8000"

 
# #set up page config
# st.set_page_config(
#     page_title = "Sepsis Prediction",
#     layout = 'wide'
# )
 
 
# #Selecting model for prediction
# def select_model():
       
#         col1,col2 = st.columns(2)
 
#         with col1:
#              selectbox = st.selectbox('Select a Model', options = ['RandomForest', 'GradientBoost'],key='selected_model')

#         with col2:
#              pass
 
#         if st.session_state['selected_model'] == 'Random Forest':
#             pipeline ='/forest_pipeline'
          
       
        
#         else:
#             pipeline = '/GradientBoost_pipeline'
 
#         st.session_state["pipeline"] = pipeline
#         return selectbox


 
# def show_form():
#     #st.title('sepsis prediction app')
#     selectbox = select_model()
 
#     with st.form('input-feature'):
#     # input fields for sepsis features
#         st.header("Input Sepsis Features ")
 
#         col1,col2 = st.tabs(["Patient Information", "Blood Work Information"])
 
#         with col1:
#             st.write ('### Patient Information')
#             st.number_input("Age", min_value= 0.0, max_value=120.0, step=0.1, key= 'age') #Age
#             st.number_input("M11", min_value= 0.0, max_value=100.0, step=0.1, key= 'm11') #BMI
#             st.selectbox("Do you have Insurance",[0,1]
#                             ,index=None,placeholder="Select 1 for Yes or 0 for No...",key = 'insurance')#Insurance
#             st.number_input("PR", min_value= 0.0, max_value=200.0, step=0.1, key= 'pr')#Blood Pressure
           
           
           
#         with col2:
#             st.write('### Blood Work Information')
#             st.number_input("PL", min_value=0.0, max_value=300.0, step=0.1, key='pl'  ) #Blood Work 1
#             st.number_input("SK", min_value= 0.0, max_value=200.0, step=0.1, key= 'sk') #Blood Work 2
#             st.number_input("TS", min_value= 0.0, max_value=1000.0, step=0.1, key= 'ts') #Blood Work 3
#             st.number_input("BD2", min_value= 0.0, max_value=10.0, step=0.1, key= 'bd2') #Blood Work 4
#             st.number_input("PRG", min_value=0.0, max_value=50.0, step=0.1, key='prg') #Plasma Glucose
           
#                 # Define a custom class for the submit button
 
           
       
#         st.form_submit_button('Predict',on_click = make_prediction)
#          # predict button
 
# def make_prediction():
#             # create dictionary with input data
#             input_data = {
#                 "PRG": st.session_state['prg'],
#                 "PL" : st.session_state['pl'],
#                 "PR" : st.session_state['pr'],
#                 "SK" : st.session_state['sk'],
#                 "TS" : st.session_state['ts'],
#                 "M11": st.session_state['m11'],
#                 "BD2": st.session_state['bd2'],
#                 "Age": st.session_state['age'],
#                 "Insurance": st.session_state['insurance']
#             }
 
            
#             #response = requests.post(f"{backend_url}/forest_pipeline, /GradientBoost_pipeline", json=input_data)
#             pipeline = st.session_state["pipeline"]
#             pipeline_url = backend_url + pipeline
            

#             # api response 
#             response = requests.post(pipeline_url, json=input_data)
 
#             # Display the prediction
#             if response.status_code == 200:
#                 prediction = response.json()['prediction']
#                 st.session_state['prediction'] = prediction
#                 probability = response.json()['probability']
#                 st.session_state['probability'] = probability
#             else:
#                 st.error(f"Error: {response.json()['detail']}")
 
# #Prediction and probability variables state at the start of the webapp
# if 'prediction' not in st.session_state:
#      st.session_state['prediction'] = None            
# if 'probability' not in st.session_state:
#      st.session_state['probability'] = None  
 
# if __name__== '__main__':
#     show_form()
#     st.write(st.session_state['prediction'])
#     st.write(st.session_state['probability'])


import streamlit as st
import requests

backend_url = "http://api-1:80"

# Set up page config
st.set_page_config(
    page_title="Sepsis Prediction",
    layout='wide'
)

# Selecting model for prediction
def select_model():
    col1, col2 = st.columns(2)

    with col1:
        selectbox = st.selectbox('Select a Model', options=['RandomForest', 'GradientBoost'], key='selected_model')

    with col2:
        pass

    if st.session_state.get('selected_model') == 'RandomForest':
        pipeline = '/forest_prediction'
    else:
        pipeline = '/gradientboost_prediction'

    st.session_state["pipeline"] = pipeline
    return selectbox


def show_form():
    selectbox = select_model()

    with st.form('input-feature'):
        st.header("Input Sepsis Features ")

        col1, col2 = st.columns([1, 1])

        with col1:
            st.write('### Patient Information')
            st.number_input("Age", min_value=0.0, max_value=120.0, step=0.1, key='age')
            st.number_input("M11", min_value=0.0, max_value=100.0, step=0.1, key='m11')
            st.selectbox("Do you have Insurance",[0,1]
                                ,index=None,placeholder="Select 1 for Yes or 0 for No...",key = 'insurance')
            st.number_input("PR", min_value=0.0, max_value=200.0, step=0.1, key='pr')

        with col2:
            st.write('### Blood Work Information')
            st.number_input("PL", min_value=0.0, max_value=300.0, step=0.1, key='pl')
            st.number_input("SK", min_value=0.0, max_value=200.0, step=0.1, key='sk')
            st.number_input("TS", min_value=0.0, max_value=1000.0, step=0.1, key='ts')
            st.number_input("BD2", min_value=0.0, max_value=10.0, step=0.1, key='bd2')
            st.number_input("PRG", min_value=0.0, max_value=50.0, step=0.1, key='prg')

        st.form_submit_button('Predict', on_click=make_prediction)


def make_prediction():
    input_data = {
        "PRG": st.session_state['prg'],
        "PL": st.session_state['pl'],
        "PR": st.session_state['pr'],
        "SK": st.session_state['sk'],
        "TS": st.session_state['ts'],
        "M11": st.session_state['m11'],
        "BD2": st.session_state['bd2'],
        "Age": st.session_state['age'],
        "Insurance": st.session_state['insurance']
    }

    pipeline = st.session_state["pipeline"]
    pipeline_url = backend_url + pipeline

    response = requests.post(pipeline_url, json=input_data)

    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.session_state['prediction'] = prediction
        probability = response.json()['probability']
        st.session_state['probability'] = probability
    else:
        st.error(f"Error: {response.json()['detail']}")


# Initialize prediction and probability variables
if 'prediction' not in st.session_state:
    st.session_state['prediction'] = None

if 'probability' not in st.session_state:
    st.session_state['probability'] = None

if __name__ == '__main__':
    show_form()
    st.write(st.session_state['prediction'])
    st.write(st.session_state['probability'])
