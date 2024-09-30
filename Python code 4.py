class EmailNotification:
    def send(self, message):
        print(f"Sending email with message: {message}")

class SMSNotifier:
    def send(self, message):
        print(f"Sending SMS with message: {message}")

class NotificationService:
    def __init__(self, email_notifier, sms_notifier):
        self.email_notifier = email_notifier
        self.sms_notifier = sms_notifier

    def send_notification(self, message):
        self.email_notifier.send(message)
        self.sms_notifier.send(message)

email_notifier = EmailNotification()
sms_notifier = SMSNotifier()
notification_service = NotificationService(email_notifier, sms_notifier)

notification_service.send_notification("Hello, world")
