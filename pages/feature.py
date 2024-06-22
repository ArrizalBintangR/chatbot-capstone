import streamlit as st
from pages.styles import page_bg_img

def show_feature():
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #55AD9B;'>Nirvita Features</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #232f3e'>Experience the future of skincare with our AI Dermatologist Assistant. Powered by advanced AWS technology, it offers personalized skin analysis, tailored treatment plans, and symptom tracking—all at your fingertips. Embrace smart, seamless, and secure dermatological care anytime, anywhere.</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h3 style='text-align: center; color: #55AD9B;'>AI Chatbot</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns([0.8, 1])

    with col1:
      st.image("https://www.aimtechnologies.co/wp-content/uploads/2023/11/AI-Chatbots.jpg", use_column_width=True)
      st.markdown("<p style='text-align: center; color: #232f3e'>AI Chatbot</p>", unsafe_allow_html=True)
      st.divider()

    with col2:
      st.markdown("<p style='text-align: left; color: #232f3e; font-size: 15px'>Our AI chatbot represents a breakthrough in digital healthcare, providing users with an interactive and intelligent conversational agent. It’s designed to understand and analyze user inquiries about skin health, offering real-time responses that are both accurate and informative. This feature enhances user engagement, reduces the need for in-person consultations, and positions our platform at the cutting edge of telemedicine. By investing in our AI chatbot, we’re not just investing in technology; we’re investing in a future where healthcare is more accessible, efficient, and user-friendly.</p>", unsafe_allow_html=True)

    st.divider()
    st.divider()

    st.markdown("<h3 style='text-align: center; color: #55AD9B;'>Image Classification</h3>", unsafe_allow_html=True)
    col3, col4 = st.columns([1, 0.8])
    with col3:
      st.markdown('<p style="text-align: right; color: #232f3e;">In the near future, our platform will be enhanced with a cutting-edge image classification feature, specifically designed for skin disease detection. This transformative technology will allow users to upload photos of their skin conditions, which our AI will analyze using deep learning algorithms to identify and classify various skin diseases. This feature promises to revolutionize the diagnosis process, offering faster, more accurate results, and empowering users with immediate insights into their skin health. Investing in this technology means investing in a pioneering solution that will lead the way in AI-driven dermatology care</p>', unsafe_allow_html=True)
  
    with col4:
      st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAjl3XTaPNB3JexzA8VHhgPca28ikmZbbAHw&s", use_column_width=True)
      st.markdown("<p style='text-align: center; color: #232f3e; font-size: 15px'>Nirvita Image Classification</p>", unsafe_allow_html=True)
# show_feature()
