import smtplib
from email.mime.text import MIMEText
from Speak import Say
#
#
# def send_email(sender_email, receiver_email, subject, body, password):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#
#     try:
#         # Use Gmail's SMTP server
#         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
#             server.login(sender_email, password)
#             server.sendmail(sender_email, receiver_email, msg.as_string())
#             Say("Email sent successfully.")
#
#     except Exception as e:
#         Say(f"Sorry, I couldn't send the email. Error: {e}")
#
# send_email("rkp8070@gmail.com","rahulkumarx333@gmail.com","check","testing","rahul@0507")
