import streamlit as st
from PIL import Image
import requests
import smtplib
import random
import os
import time
import datetime

from email_validator import validate_email, EmailNotValidError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from io import BytesIO
from PIL import Image
from streamlit_js_eval import streamlit_js_eval
from pages.styles import page_bg_img

team_names = ["Arrizal Bintang Ramadhan", "Icut Like Aprilliyana", "Muhammad Fatih Khaeran Rabbani", "Salsabila Anisah Putri Farihah", "Rafi Zhafar Kurnia", "Nurul Ajijah Kartika Dewi", "Moch. Sultan Fauzi"]

## Load secrets.toml variables for email configuration
options = os.getenv("OPTIONS")
server = os.getenv("SERVER")
port = os.getenv("PORT")
u = os.getenv("U")
secret = os.getenv("SECRET")
recipient = os.getenv("RECIPIENT")

def show_about():
  st.markdown(page_bg_img, unsafe_allow_html=True)
  st.markdown(f"<h1 style='text-align: center; color: #55AD9B;'>About Nirvita</h1>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: center; color:#232f3e;'>At Nirmala Vitalis, our philosophy is rooted in the promotion of clean and pure health, fostering a life of sustainable vitality. 'Nirmala' signifies the essence of purity and cleanliness, while 'Vitalis' captures the crucial life force that propels us. Together, they encapsulate our commitment to nurturing a holistic well-being that resonates with the natural balance of life.</p>", unsafe_allow_html=True)

#############################################################################################################
  st.markdown("<h2 style='text-align: center; color: #55AD9B;'>Our Team</h2>", unsafe_allow_html=True)

  row1 = st.columns(3)
  row2 = st.columns(4)

  # Assuming row1 and row2 are lists of Streamlit columns
  #TODO : cache the images using cloudfront

  # Loop through columns and display images with styled captions
  for index, col in enumerate(row1 + row2):
    image_url = f'https://potokelompok.s3.ap-southeast-1.amazonaws.com/{index + 1}'
    image = Image.open(requests.get(image_url, stream=True).raw)
    new_image = image.resize((250, 250))
    
    # Convert image to base64 for embedding in HTML
    from io import BytesIO
    import base64
    
    buffered = BytesIO()
    new_image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    img_data = f"data:image/png;base64,{img_str}"
    
    # HTML to display image with styled caption
    caption = team_names[index]
    html_code = f"""
    <div style="text-align: center;">
        <img src="{img_data}" alt="{caption}" style="width: 100%; height: auto;">
        <div style="color: grey;">{caption}</div>
    </div>
    """
    col.markdown(html_code, unsafe_allow_html=True)

#############################################################################################################
  st.markdown("<h2 style='text-align: center; color: #55AD9B;'>✉️ Contact Us</h2>", unsafe_allow_html=True)

  col1, col2, col3, col4 =  st.columns([150, 0.25, 1, 0.25]) # column widths for a balanced distribution of elements in the page
  ## Contact form
  with col1: # left side of the layout
      email = st.text_input(":grey[**Your Email***]", value=st.session_state.get('email', ''), key='email', help='color:#232f3e') # input widget for contact email
      message = st.text_area(":grey[**Your Message***]", value=st.session_state.get('message', ''), key='message', help='color:#232f3e') # input widget for message

      st.markdown('<p style="font-size: 13px; color: #232f3e">*Required fields</p>', unsafe_allow_html=True) # indication to user that both fields must be filled

  spacer1, button_col, spacer2 = st.columns([1.5, 1, 1])

  with spacer1:
      # This is just a spacer
      st.write("")

  with button_col:
    if st.button("Send", type="primary"):
        if not email or not message:
            st.error("Please fill out all required fields.") # error for any blank field
        else:
            try:
                # Robust email validation
                valid = validate_email(email, check_deliverability=True)

                # Check CAPTCHA
                if captcha_input.upper() == captcha_text:

                    # Email configuration - **IMPORTANT**: for security these details should be present in the "Secrets" section of Streamlit
                    #### NOTE FOR DEVELOPERS: UNCOMMENT THE LINES BELOW ####
                    
                    #smtp_server = server
                    #smtp_port = port
                    #smtp_username = u
                    #smtp_password = secret
                    #recipient_email = recipient

                    ## Create an SMTP connection
                    #server = smtplib.SMTP(smtp_server, smtp_port)
                    #server.starttls()
                    #server.login(smtp_username, smtp_password)

                    ## Compose the email message
                    #subject = "Contact Form Submission" # subject of the email you will receive upon contact.
                    #body = f"Email: {email}\nMessage: {message}"
                    #msg = MIMEMultipart()
                    #msg['From'] = smtp_username
                    #msg['To'] = recipient_email
                    #msg['Subject'] = subject
                    #msg.attach(MIMEText(body, 'plain'))

                    ## Send the email
                    #server.sendmail(smtp_username, recipient_email, msg.as_string())

                    ## Send the confirmation email to the message sender # If you do not want to send a confirmation email leave this section commented
                    #current_datetime = datetime.datetime.now()
                    #formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    #confirmation_subject = f"Confirmation of Contact Form Submission ({formatted_datetime})"
                    #confirmation_body = f"Thank you for contacting us! Your message has been received.\n\nYour message: {message}"
                    #confirmation_msg = MIMEMultipart()
                    #confirmation_msg['From'] = smtp_username
                    #confirmation_msg['To'] = email  # Use the sender's email address here
                    #confirmation_msg['Subject'] = confirmation_subject
                    #confirmation_msg.attach(MIMEText(confirmation_body, 'plain'))
                    #server.sendmail(smtp_username, email, confirmation_msg.as_string())

                    ## Close the SMTP server connection
                    #server.quit()

                    #st.success("Sent successfully!") # Success message to the user.
                    
                    #### NOTE FOR DEVELOPERS: UPON DEPLOYMENT DELETE THE SECTION BELOW ####
                    st.info("""This would have been a message sent successfully!  
                    For more information on activating the contact form, please check the [documentation](https://github.com/jlnetosci/streamlit-contact-form).""") # Please delete this info box if you have the contact form setup correctly.

                    # Generate a new captcha to prevent button spamming.
                    st.session_state.captcha_text = generate_captcha()
                    captcha_text, captcha_image = st.session_state.captcha_text
                    # Update the displayed captcha image
                    captcha_placeholder.image(captcha_image, use_column_width=True)

                    time.sleep(3)
                    streamlit_js_eval(js_expressions="parent.window.location.reload()")

            except EmailNotValidError as e:
                st.error(f"Invalid email address. {e}") # error in case any of the email validation checks have not passed
