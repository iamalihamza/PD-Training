''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib, ssl
import os
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import logging

# Set up email server credentials

email_address = 'abc@gmail.com'
email_password = '***'  # add your gmail App password instead of regular password
smtp_server = "smtp.gmail.com"  # using server for gmail
smtp_port = 465

# Set up report file path and recipients
report_path = "report file.txt"
recipients = ["xyz@gmail.com", "xyz2@gmail.com"]

# Set up email contents
subject = "Daily Report"
body = "Please find attached the daily report."
attachment_name = os.path.basename(report_path)  # fetching the name for report file which will be sent
attachment = MIMEApplication(open(report_path, 'rb').read(), _subtype='txt')  # reading the content of that file

# adds a header to the attachment object specifying that it should be treated as an attachment with a filename of
# attachment_name.
attachment.add_header('Content-Disposition', 'attachment', filename=attachment_name)
msg = MIMEMultipart()
msg['From'] = email_address
msg['Subject'] = subject
msg.attach(MIMEText(body))
msg.attach(attachment)


# Define email sending function
def send_email():
    try:
        # opening SSL connection
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as server:
            server.login(email_address, email_password)  # logging in with email and password after opening a connection
            for recipient in recipients:  # iterating the recipients list to send mail to all of them
                msg['To'] = recipient
                server.sendmail(email_address, recipient, msg.as_string())  # sending the email
                print(f"Report sent to {recipient} successfully!")
                logging.info(f"Report sent to {recipient} successfully!")  # saved the entry for email success
            server.quit()  # closing the connection after using it
    except Exception as e:
        print(f"Error sending email: {e}")


# Schedule email sending at a specific time each day
schedule.every().day.at("09:30").do(send_email)
# schedule.every(2).minutes.do(send_email)  # for testing

# all the logging will be written in report_sender.log
logging.basicConfig(filename='report_sender.log', level=logging.INFO)

# Main loop
while True:
    try:
        schedule.run_pending()  # it will trigger the scheduler that run send_email
        time.sleep(1)
    except Exception as e:
        logging.error(f"Error sending report: {e}")  # all the errors will be reported in report_sender.log
