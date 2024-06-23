import streamlit as st
from pages.styles import page_bg_img


def show_home():
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #55AD9B;'>Nirvita, AI Dermatologist Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #232f3e;'>Powered By AWS☁️ & Streamlit🔻</h2>", unsafe_allow_html=True)
    columns = st.columns((2, 1, 2))
    button_pressed = columns[1].button(':green[Try Now !]')
    if button_pressed:
        st.switch_page("pages/chatbot.py")

    st.divider()
    st.markdown("<h3 style='color: #232f3e;'>Why choose Nirvita?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #232f3e;'>Nirvita is a cutting-edge AI dermatologist assistant that offers personalized skin analysis, tailored treatment plans, and symptom tracking. It leverages advanced AWS technology to provide users with accurate skin health advice, potential diagnoses, and treatment options. By investing in Nirvita, you’re investing in a future where skincare is smart, seamless, and secure. Experience the next generation of dermatological care with Nirvita today.</p>", unsafe_allow_html=True)

    st.markdown("<h3 style='color: #232f3e;'>What is a dermatologist?</h3>", unsafe_allow_html=True)
    st.write("<p style='color: #232f3e;'>A dermatologist is a doctor who specializes in conditions involving the skin, hair, and nails. The skin is an incredible organ. It is the largest organ in the body and the first line of defense against disease and infection. It is also the only organ that is constantly exposed to the environment. As a result, the skin is susceptible to a wide range of conditions. Dermatologists are experts in diagnosing and treating these conditions. They can help you keep your skin healthy and beautiful.</p>", unsafe_allow_html=True)

    st.markdown("<h3 style='color: #232f3e;'>What Does AI In Dermatology Look Like?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #232f3e;'>AI in dermatology is a game-changer. It uses cutting-edge algorithms to analyze skin conditions, compare them with vast dermatological datasets, and provide accurate assessments. This empowers users with instant access to skin health advice, potential diagnoses, and treatment options. By integrating AI, we’re not just solving skin problems—we’re transforming the skincare journey into a seamless, tech-driven experience.</p>", unsafe_allow_html=True)

    st.markdown("<h3 style='color: #232f3e;'>How does Artificial Intelligence helps you Answer your Skin problem?</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #232f3e;'>Artificial Intelligence revolutionizes dermatology by offering precise, personalized, and proactive skin care solutions. Our AI dermatologist assistant leverages cutting-edge algorithms to analyze skin conditions, compare them with vast dermatological datasets, and provide accurate assessments. It empowers users with instant access to skin health advice, potential diagnoses, and treatment options. This not only enhances patient engagement and satisfaction but also streamlines the workload of healthcare professionals. By integrating AI, we’re not just solving skin problems—we’re transforming the skincare journey into a seamless, tech-driven experience.</p>", unsafe_allow_html=True)

