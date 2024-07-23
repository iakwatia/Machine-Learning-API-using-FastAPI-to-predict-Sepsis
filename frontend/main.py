
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
