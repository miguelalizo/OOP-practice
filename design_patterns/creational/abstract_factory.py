"""
Multi-Channel Notification Service.

It will support Email, SMS, and Push notification.
Our service also integrates with two different imaginary
notification SAAS providers: FastNotif and SendBlue.
"""

from abc import ABC, abstractmethod
from enum import Enum


# 0. Abstract Factory Interface
class NotificationFactory(ABC):
    """
    This interface enforces a consistent structure for factories,
    ensuring that they can create various types of notification,
    whether its for email, SMS, or push notification.

    Concrete factories, such as FastNotifFactory and SendBlueFactory,
    must implement these methods to fulfill the contract defined by
    the NotificationFactory interface.
    """

    @abstractmethod
    def create_email_notification(self):
        pass

    @abstractmethod
    def create_sms_notification(self):
        pass

    @abstractmethod
    def create_push_notification(self):
        pass


# 1. Define Concrete Factories
class FastNotifFactory(NotificationFactory):
    def create_email_notification(self):
        return FastNotifEmailNotification()

    def create_sms_notification(self):
        return FastNotifSMSNotification()

    def create_push_notification(self):
        return FastNotifPushNotification()


class SendBlueFactory(NotificationFactory):
    def create_email_notification(self):
        return SendBlueEmailNotification()

    def create_sms_notification(self):
        return SendBlueSMSNotification()

    def create_push_notification(self):
        return SendBluePushNotification()


# 2. Define Abstract Product Classes
class AbstractEmailNotification(ABC):
    """Abstract product for Email notification"""

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_content(self):
        pass


# 2. Define Abstract Product Classes
class AbstractSMSNotification(ABC):
    """Abstract product for SMS notification"""

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_content(self):
        pass


# 2. Define Abstract Product Classes
class AbstractPushNotification(ABC):
    """Abstract product for Push notification"""

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def format_content(self):
        pass


# 3. Define Concrete Product Classes
class FastNotifEmailNotification(AbstractEmailNotification):
    """Concrete product for FastNotif Email notification"""

    def send(self):
        print("FastNotif: sending Email notification")

    def format_content():
        print("FastNotif: formatting Email content")


class FastNotifSMSNotification(AbstractSMSNotification):
    """Concrete product for FastNotif SMS notification"""

    def send(self):
        print("FastNotif: sending SMS notification")

    def format_content():
        print("FastNotif: formatting SMS content")


class FastNotifPushNotification(AbstractPushNotification):
    """Concrete product for FastNotif Push notification"""

    def send(self):
        print("FastNotif: sending Push notification")

    def format_content():
        print("FastNotif: formatting Push content")


class SendBlueEmailNotification(AbstractEmailNotification):
    """Concrete product for SendBlue Email notification"""

    def send(self):
        print("SendBlue: sending Email notification")

    def format_content():
        print("SendBlue: formatting Email content")


class SendBlueSMSNotification(AbstractSMSNotification):
    """Concrete product for SendBlue SMS notification"""

    def send(self):
        print("SendBlue: sending SMS notification")

    def format_content():
        print("SendBlue: formatting SMS content")


class SendBluePushNotification(AbstractPushNotification):
    """Concrete product for SendBlue Push notification"""

    def send(self):
        print("SendBlue: sending Push notification")

    def format_content():
        print("SendBlue: formatting Push content")


# 4. Factory Mapping (dictionary dispatch, with enumerated keys)
class NotificationType(Enum):
    FastNotif = "FastNotif"
    SendBlue = "SendBlue"


factory_mapping = {
    NotificationType.FastNotif: FastNotifFactory(),
    NotificationType.SendBlue: SendBlueFactory(),
}


def select_notification(provider: NotificationType) -> NotificationFactory:
    """Select and return Notification Factory based on the provider"""
    factory = factory_mapping.get(provider)
    if factory is None:
        raise ValueError("Invalid provider")
    return factory


if __name__ == "__main__":
    # client code

    fast_notif = select_notification(NotificationType.FastNotif)
    # send email notification through FastNotif
    fast_notif.create_email_notification().send()
    # send SMS notification through FastNotif
    fast_notif.create_sms_notification().send()
    # send Push notification through FastNotif
    fast_notif.create_push_notification().send()

    send_blue = select_notification(NotificationType.SendBlue)
    # send email notification through BlueNotif
    send_blue.create_email_notification().send()
    # send SMS notification through BlueNotif
    send_blue.create_sms_notification().send()
    # send Push notification through BlueNotif
    send_blue.create_push_notification().send()
