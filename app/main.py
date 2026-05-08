from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

# Changing the color and bg-color of app
st.markdown("""
<style>
.stApp {
    background-color: #515d7d;
    color: white;
}
</style>
""", unsafe_allow_html=True)

def get_guess(input_df: pd.DataFrame) -> int:
    """ Gets models directory path, loads joblib file and returns result (1 or 0) """
    models_dir = Path(__file__).parent.parent / "models"
    get_model = joblib.load(models_dir / "brain.joblib")
    return get_model.predict(input_df)[0]

st.title("Lets find out she will like you or not based on:")
st.metric(label="Model Accuracy on our dataset", value="85%")
st.divider()
columns = ["Look_Score_You","Look_Score_Her","Relationship_Score","Your_Social_Score","Her_Social_Score","Probability"]
lsy = st.number_input("Rate yourself based on looks (?/10)", min_value=0, max_value=10, step=1)
lsh = st.number_input("Rate her based on looks (?/10)", min_value=0, max_value=10, step=1)
rs = st.number_input("Rate your relationship (0: We haven't met / 10: We are close friends)", min_value=0, max_value=10, step=1)
yss = st.number_input("Rate your social skills (Making jokes, number of friends etc.)", min_value=0, max_value=10, step=1)
hss = st.number_input("Rate her social skills (Being friendly and sincere etc.)", min_value=0, max_value=10, step=1)
prob = st.number_input("Rate the probability of you two dating (?/10)", min_value=0, max_value=10, step=1)

if st.button("Predict"):
    result = get_guess(pd.DataFrame([[lsy, lsh, rs, yss, hss, prob]], columns=columns))
    if result == 1:
        st.success("'She likes you or she will'; says Machine.")
    else:
        st.error("Sorry mate but you need to find somebody else..")