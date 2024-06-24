import streamlit as st
from PIL import Image
import pickle

pickle_in = open("svc1_new_model.pkl", "rb")
classifier = pickle.load(pickle_in)

# @ app.route('/')
def welcome():
    return "Welcome All"

# @app.route ('/predict',method=['get'])
def predict_note_authentication(Hour, Day, Month, Dayofweek):
    """Let us resolve the problem of call center, contact center, complaint center,
    service providers to predict the number of incoming calls Hour, Day, Month, Day of Week.
    parameter:
      - name : Hour
        in: query
        type: number
        required: True
      - name : Day
        in: query
        type: number
        required: True
      - name : Month
        in: query
        type: number
        required: True
      - name : Day of week
        in: query
        type: number
        required: True
    responses:
        200:
            description: The output values        
    """
    prediction= classifier.predict([[Hour, Day, Month, Dayofweek]])
    print(prediction)
    return prediction

def main():
    st.title("Machine Learning Model")
    st.title("Incoming Calls Predictor")

    html_temp = """
    <div style="background-color:purple;padding:10px">
    <h2 style="color=white;text-align:center;">ML Model design for 
    Call Center, Contact Center, Complaint Center & Service Center </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Hour = st.text_input("Hour", "Type Here")
    Day = st.text_input("Day", "Type Here")
    Month = st.text_input("Month", "Type Here")
    Dayofweek = st.text_input("Dayofweek", "Type Here")
    result= ""
    if st.button("Predict"):
        result= predict_note_authentication(Hour, Day, Month, Dayofweek)
    st.success("The output is {}".format(result))
    st.text("Contact to customize one for your company")
    st.text("Name: Uzair Ahmed")
    st.text("Email: uzairrajput100@gmail.com")

if __name__=="__main__":
    main()

