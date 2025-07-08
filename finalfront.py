import streamlit as st
import pickle
import numpy as np
import time
import joblib
import base64
import matplotlib.pyplot as plt
import pandas as pd


import seaborn as sns

# Function to set background image
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            h1, h2, h3 {{
            font-family: 'Carl Brown', sans-serif;
            color: #EC5228; /* Orange text */
            background: rgba(0, 0, 0, 0.8); /* Black background */
            padding: 12px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.5); /* Black shadow */
            margin-top: 10px;
            margin-bottom: 20px;
            
            }}





            
        }}
        .main {{
        background-color: rgba(10, 10, 10, 0.5);
            # background-color: rgba(255, 207, 241, 0.5);
            padding: 10px;
            border-radius: 15px;
            color:#f0f2f6; 
        }}
        .sidebar .sidebar-content {{
            background-color: #C54B8C;
            color: Black;
        }}
        h1, h2, h3 {{
            font-family: 'Carl Brown', sans-serif;
            color: #EC5228;
        }}
        .footer {{
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #C54B8C;
            color: Black;
            text-align: center;
            padding: 10px;
        }}
        /* Input Field Customization */
        .st-emotion-cache-ue6h4q {{color: #f0f2f6}}
       .st-emotion-cache-1vxmjmh .st-bq + .st-c0 {{color: #f0f2f6}}
        .st-bq .st-emotion-cache-187vdiz {{color: #f0f2f6}}
       .st-emotion-cache-1vxmjmh button {{color: black}}
       .st-dz {{background-color: rgba(33, 195, 84, 0.6);}}
       .st-ds {{color:#3cf309;}}
       .st-ea {{background-color: rgba(255, 43, 43, 0.6);}}
       .st-e9 {{color:#25090b;}}
        
        div.stNumberInput input {{
            background-color: #EC5228 ; /* Light gray background */
            #color: #333 !important; /* Dark text */
           # border-radius: 10px; /* Rounded corners */
            #border: 2px solid #ff69b4 !important; /* Pink border */
            #padding: 8px; /* Padding */
        }}
        #div.stNumberInput input:focus {{
            #border-color: #ff1493 !important; /* Deep pink focus */
            #box-shadow: 0px 0px 10px rgba(255, 20, 147, 0);
        #}}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to display GIF
def show_gif(gif_path, width=200):
    gif_data = open(gif_path, "rb").read()
    base64_gif = base64.b64encode(gif_data).decode("utf-8")
    st.markdown(
        f'<img src="data:image/gif;base64,{base64_gif}" width="{width}"/>',
        unsafe_allow_html=True,
    )

# Apply background (Change to your correct image path)
set_background(r"C:\Users\Ishika\project\image_file.jpeg")

def show_gif(gif_path, width=200):
    gif_data = open(gif_path, "rb").read()
    base64_gif = base64.b64encode(gif_data).decode("utf-8")
    return f'<img src="data:image/gif;base64,{base64_gif}" width="{width}"/>'

 
    
# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(" ", ["Home", "Prediction"])

# Home Page
if page == "Home":
    st.title("👩‍⚕️ Welcome to PCOS/PCOD Detection System")
    st.write(
        """
        **This system helps detect the likelihood of PCOS/PCOD based on various input factors.
        Please navigate to the Prediction page to proceed with the diagnosis.**




        
        **Polycystic Ovary Syndrome (PCOS) and Polycystic Ovarian Disorder (PCOD) are common yet complex hormonal disorders affecting millions of women worldwide.**" 
        **Early detection and management are crucial for maintaining a healthy lifestyle.**


        """ 


    )
# Add histogram plot
    st.subheader("📊 Symptom Distribution by Age pcos_pcod_analysis_results.xlsx dataset")
    
    # Generate the Seaborn histogram
    df=pd.read_excel(r'C:\Users\Ishika\project\pcos_pcod_analysis_results.xlsx')
# def plot_symptom_distribution():
#     fig, ax = plt.subplots(figsize=(8, 6))
#     sns.histplot(data=df, x='age', hue='unusual_bleeding', bins=10, kde=True, alpha=0.8, ax=ax)
#     ax.set_title("Symptom Distribution by Age")
#     ax.set_xlabel("Age")
#     ax.set_ylabel("Frequency")
#     return fig



# def plot_age_distribution():
#     fig, ax = plt.subplots(figsize=(10, 6))
#     sns.histplot(data=df, x='age', hue='pcos_pcod_risk', bins=10, kde=True, alpha=0.8, ax=ax)
#     ax.set_title("Age-wise Distribution of PCOS/PCOD Risk")
#     ax.set_xlabel("Age")
#     ax.set_ylabel("Frequency")
#     return fig

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data=df, x='age', hue='pcos_pcod_risk', bins=10, kde=True, ax=ax,alpha=1)

    # ax.set_title("Symptom Distribution by Age ")
    # ax.set_xlabel("Age")
    # ax.set_ylabel("Frequency")
# Add the first graph
    # st.subheader("📊 Symptom Distribution by Age")
    # fig1 = plot_symptom_distribution()
    # st.pyplot(fig1)
    
    # Add the second graph
    st.subheader("📊 Age-wise Distribution of PCOS/PCOD Risk")
    # fig2 = plot_age_distribution()
    st.pyplot(fig)
    
    


    # st.subheader("📊 Age-wise Distribution of PCOS/PCOD Risk")
    # fig = plot_age_distribution()
    # # Display the plot in the app
    # st.pyplot(fig)
    # st.pyplot(fig1)

# Prediction Page
if page == "Prediction":
    st.title("🩺 PCOS/PCOD Detection System")

    # User input fields
    age = st.number_input("**Age**", min_value=10, max_value=50, value=25)
    weight = st.number_input("**Weight (kg)**", min_value=30.0, max_value=150.0, value=55.0)
    height = st.number_input("**Height (cm)**", min_value=120.0, max_value=200.0, value=160.0)
    
    # BMI Calculation
    bmi = weight / ((height / 100) ** 2)
    st.write(f"**📊 Calculated BMI: {bmi:.2f}**")

    length_of_cycle = st.number_input("**Menstrual Cycle Length (days)**", min_value=20, max_value=45, value=28)
   
    # Additional symptoms
    unusual_bleeding = st.radio("**Do you have unusual bleeding?**", ["Yes", "No"])

    # Convert inputs into numerical format
    unusual_bleeding = 1 if unusual_bleeding == "Yes" else 0
    
    # Prepare input features
    input_features = np.array([[age, length_of_cycle, unusual_bleeding, bmi]])

    # Load the trained model
    model = joblib.load("logistic_regression_model.pkl")

    # # Prediction button
    if st.button("🔍 Predict"):
        placeholder = st.empty()  # Create a placeholder for the analyzing GIF
        placeholder.markdown(show_gif(r"C:\Users\Ishika\project\code thinking.gif", width=250), unsafe_allow_html=True)  # Show analyzing GIF
        with st.spinner("**⏳ Analyzing... Please wait!**"):
             time.sleep(3)  # Simulate prediction loading time

        # Predict using the loaded model
        prediction = model.predict(input_features)

        result = "✅ Likely to have PCOS" if prediction[0] == 1 else "❌ Unlikely to have PCOS"
         # Remove analyzing GIF
        placeholder.empty()
            # Predict using the loaded model
        prediction = model.predict(input_features)

        # Display prediction result
        if prediction[0] == 1:
            st.success("**🩺 Prediction: ✅ Likely to have PCOS/PCOD**")
            placeholder = st.empty() 
            placeholder.markdown(show_gif(r"C:\Users\Ishika\project\code consoling.gif", width=250),unsafe_allow_html=True)  # Consoling face GIF
            
        else:
            st.error("**🩺 Prediction: ❌ Unlikely to have PCOS/PCOD**")
            placeholder = st.empty() 
            placeholder.markdown(show_gif(r"C:\Users\Ishika\project\code happy.gif", width=250),unsafe_allow_html=True ) # Happy face GIF

    # Footer
    st.markdown(
        """
        <div class="footer">
            🎯 Developed using Streamlit and Python | © 2025
        </div>
        """,
        unsafe_allow_html=True,
    )