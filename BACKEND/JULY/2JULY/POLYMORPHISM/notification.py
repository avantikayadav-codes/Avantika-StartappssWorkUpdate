class EmailNotification:
    def send(self):
        print("Email Notification Sent")


class SMSNotification:
    def send(self):
        print("SMS Notification Sent")


class PushNotification:
    def send(self):
        print("Push Notification Sent")


def notify(notification):
    notification.send()


e = EmailNotification()
s = SMSNotification()
p = PushNotification()

notify(e)
notify(s)
notify(p)