import requests, os
# import smtplib



class Contact:
    def __init__(self):
        self.my_email = os.getenv('MY_EMAIL')
        self.end_point = os.getenv('END_POINT')
    #     self.password = os.getenv('EMAIL_PASSWORD')
    #
    # def send_email(self, data):
    #     msg = f"Subject:Blog_response\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['number']}\nMessage: {data['message']}"
    #     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #         connection.starttls()
    #         connection.login(user=self.my_email, password=self.password)
    #         connection.sendmail(from_addr=self.my_email, to_addrs=self.my_email,
    #                             msg=msg.encode())


    # def send_email(self, data):
    #     email = {
    #         "title": "Blog_response",
    #         "html": f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['number']}\nMessage: {data['message']}",
    #         "recipients": [{"email": os.getenv('MY_EMAIL'), "name": "test"}]
    #     }
    #     response = requests.request('POST', url=self.end_point, headers=self.headers, json=email)


    def send_simple_message(self, data):
        return requests.post(self.end_point,
                             auth=("api", os.getenv('KEY')),
                             data={"from": self.my_email,
                                   "to": [self.my_email],
                                   "subject": "Blog Response",
                                   "text": f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['number']}\nMessage: {data['message']}"})





