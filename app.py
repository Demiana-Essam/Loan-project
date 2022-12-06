import streamlit as st
import joblib 
import pandas as pd
import base64

Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")
df = pd.read_csv("EDA_OUT.csv")

def predict(Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term, Credit_History, Property_Area):
    
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"ApplicantIncome"] = ApplicantIncome
    test_df.at[0,"CoapplicantIncome"] = CoapplicantIncome
    test_df.at[0,"LoanAmount"] = LoanAmount
    test_df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    test_df.at[0,"Credit_History"] = Credit_History
    test_df.at[0,"Property_Area"] = Property_Area
    
    result = Model.predict(test_df)[0]
    
    return result
    
    
def main():
    
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            st.markdown(
           f"""
           <style>
           .stApp {{
               background-image: url(data:image/{"ipg"};base64,{encoded_string.decode()});
               background-size: cover
           }}
           </style>
           """,
           unsafe_allow_html=True
           )
    add_bg_from_local('back9.jpg')

    st.markdown("## Predict If Loan Will Be Approved Or Not  ")
    st.markdown('______________________________________')
    col1, col2 = st.columns(2)
    
    with col1:
        
        Gender = st.selectbox('Select the applicant gender ',df['Gender'].unique())
        Married = st.selectbox('Select if the applicant is married or not',df['Married'].unique())
        Dependents = st.selectbox('Select number of Dependents for this Applicant ', df['Dependents'].unique())
        Education = st.selectbox("Select if the applicant is educated or not ",df['Education'].unique())
        Self_Employed = st.selectbox('Select if the applicant is Self_Employed or not', df['Self_Employed'].unique())
        Credit_History = st.selectbox('Select 1 if applicant Credit_History is good', df['Credit_History'].unique())
        
        
    with col2:
        ApplicantIncome = st.slider("Applicant Income" , min_value=0, max_value=81000, value=0, step=1)
        CoapplicantIncome = st.slider("Coapplicant Income" , min_value=0, max_value=41667, value=0, step=1)
        LoanAmount = st.slider("LoanAmount in thousands" , min_value=0, max_value=1000, value=0, step=1)
        Loan_Amount_Term =st.slider("Loan Amount Term in months" , min_value=12, max_value=480, value=12, step=12)
        Property_Area = st.selectbox('Select the Property Area',df['Property_Area'].unique())

    with col1:
        if st.button(' Predict '):
            
            result = predict(Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome, CoapplicantIncome, LoanAmount,Loan_Amount_Term, Credit_History, Property_Area)
            #label = ["Loan cannot be approved ","Loan will be approved "]
            #st.text("The Prediction is {}".format(label[result]))
            if result == 1:
                res = '<p style="font-family:Verdana;color:#4BFF58; font-size: 20px;">Loan will be approved😊</p>'
                st.markdown(res,unsafe_allow_html=True)
            elif result == 0:
                res = '<p style="font-family:Verdana; color:#FF4B4B; font-size: 20px;">Loan cannot be approved 🥺</p>'
                st.markdown(res,unsafe_allow_html=True)    
            
            
if __name__ == '__main__':
    main()    
    
