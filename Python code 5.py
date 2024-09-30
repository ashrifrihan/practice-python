from abc import ABC, abstractmethod

# Abstraction
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Concrete implementations
class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Sending email with message: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Sending SMS with message: {message}")

# High-level module depends on the abstraction
class NotificationService:
    def __init__(self, notifiers):
        self.notifiers = notifiers

    def send_notification(self, message):
        for notifier in self.notifiers:
            notifier.send(message)

# Usage
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
notifiers = [email_notifier, sms_notifier]
notification_service = NotificationService(notifiers)
notification_service.send_notification("Hello, World!")