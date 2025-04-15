import streamlit as st

st.title("💪 Simple BMI Calculator")

height = st.number_input("Enter your height (in meters)", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight (in kilograms)", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.info("You are Underweight.")
        elif 18.5 <= bmi < 25:
            st.success("You are Normal weight.")
        elif 25 <= bmi < 30:
            st.warning("You are Overweight.")
        else:
            st.error("You are Obese.")
    else:
        st.error("Please enter valid height and weight.")
