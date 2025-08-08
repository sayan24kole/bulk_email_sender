from flask import Flask, request, render_template
#import os
import smtplib
from email.message import EmailMessage
import time
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('webpage_email.htm')
    '''print("Current working directory:", os.getcwd())
    return render_template('webpage_email.html')'''
@app.route('/process', methods=['POST'])
def process():
    email1 = request.form['email1']
    email2 = request.form['email2']
    password = request.form['password']
    subject = request.form['subject']
    body = request.form['body']
    total_count = int(request.form['count'])
    seconds = int(request.form['seconds'])
    EMAIL_ADDRESS = email1
    EMAIL_PASSWORD = password
    TO_EMAIL = email2
    SUBJECT = subject
    BODY = body
    REPEAT_COUNT = total_count
    DELAY_SECONDS = seconds  
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT
    msg.set_content(BODY)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        for i in range(REPEAT_COUNT):
            smtp.send_message(msg)
            print(f'Email {i+1} sent.')
            time.sleep(DELAY_SECONDS)

    print('done')
    return f"<h1>Successfully sent {REPEAT_COUNT} emails to {TO_EMAIL}!</h1>"


if __name__ == '__main__':
    app.run(debug=True)