#streamlit
import streamlit as st

st.set_page_config(page_title="growth mindset project", project_icon="★")
st.title("Groth Mindset Challenge: web app with streamlit")

st.header("✶ Welcome to your growth journey!")
st.write("Embrace challenges,learn from mistakes,and unlock your full potential.This AI-powered app help you build a growth mindset with reflection, challenges, and achievements!🌟")

#qoute section
st.header("💡Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.\"-winston churchill\"")

st.header("🔧What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


#condition
if user_input:
    st.success(f"🥸you're facing:{user_input}.keep pushing forward towords your goal!🥷")
else:
    st.warning("tell as about your challenge to get started!") 

 #reflexing
st.header("Reflect on your learning")
reflection = st.text_area("write your reflection here:")

if reflection:
    st.success(f"✨Great Insight! Your reflection:{reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")


#acheivements
st.header("✌️Celebrate YOUR Wins!")
acheivment =st.text_input("share something you've recently accomlished")


if acheivment:
    st.success(f"🎉 Amazing you achieved:{acheivment}")
else:
    st.info("big or small , every acheivment counts! share one now!😍")    


#footer
st.write("- - -")
st.write("🚀keep believing in yourself. Growth is a journey, not a destination!🌟")
st.write("**😇 created by Sajid Ali")
