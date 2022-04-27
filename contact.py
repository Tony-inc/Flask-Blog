import os
import smtplib
from boto.s3.connection import S3Connection


class Contact:
    def __init__(self):
        self.my_email = S3Connection(os.environ['MY_EMAIL'])
        self.password = S3Connection(os.environ['EMAIL_PASSWORD'])

    def send_email(self, data):
        msg = f"Subject:Blog_response\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['number']}\nMessage: {data['message']}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr=self.my_email, to_addrs=self.my_email,
                                msg=msg.encode())
