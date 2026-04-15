#Real-world Polymorphism
#Task:
#Create Notification system (Email, SMS, Push).

class email:
    def send(self):
        print("sending email")
    
class sms:
    def send(self):
        print("sending sms")

class push:
    def send(self):
        print("sending push")

def notify(user_msg):
   user_msg.send()

notify(email())
notify(sms())
notify(push())