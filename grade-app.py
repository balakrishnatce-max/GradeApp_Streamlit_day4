import streamlit as st

st.title("Grade Calculator")
st.write("This application calculates your grade based on your mark.")

score = st.number_input("Enter your mark:",min_value=0.0, max_value=100.0, step=0.1)

if score >= 90:
    st.success("You have an A grade.")
    st.chat_message("assistant").write("Excellent work!")
    st.balloons()
elif score >= 80:
    st.info("You have a B grade.")
    st.chat_message("assistant").write("Keep up the good work!")
elif score >= 70:
    st.warning("You have a C grade.")
    st.chat_message("assistant").write("You can do better!")
elif score >= 60:
    st.error("You have a D grade.")
    st.chat_message("assistant").write("You need to improve!")  
else:
    st.error("You have an E grade.")
    st.chat_message("assistant").write("You need to work hard!")
    st.feedback()