from __future__ import annotations
from typing import Set, List


class User:
    """
    User class for Chat system.

    Subscriber to NotificationService
    """

    def __init__(self, name: str):
        self.name = name
        self.friends: Set[User] = set()
        self.chats: Set[ChatRoom] = set()
        self.friend_requests: Set[User] = set()
        self.chat_invites: Set[ChatRoom] = set()
        self.notifications: List[str] = []

    def send_friend_request(self, user: User) -> None:
        user.queue_friend_request(self)

    def queue_friend_request(self, user: User) -> None:
        self.friend_requests.add(user)

    def queue_chat_invite(self, chat: ChatRoom):
        self.chat_invites.add(chat)
        print(f"User {self}: invited to {chat}")

    def accept_chat_invite(self, chat: ChatRoom):
        if chat not in self.chat_invites:
            raise Exception(f"Was not invited to {chat.name}")
        self.chat_invites.remove(chat)
        chat.add_member(self)

    def accept_friend_request(self, user: User):
        if user not in self.friend_requests:
            raise Exception(f"Friend Request Error {user} did not send a request")
        user.friends.add(self)
        self.friends.add(user)
        self.friend_requests.pop(user)

    def remove_friend(self, user: User) -> None:
        if user not in self.friends:
            raise Exception(f"{user.name} is not a friend of {self.name}")
        self.friends.remove(user)

    def join_chat(self, chat: ChatRoom):
        self.chats.add(chat)

    def leave_chat(self, chat: ChatRoom):
        if chat not in self.chats:
            raise Exception(f"User is not a member of {chat.name}")
        self.chats.remove(chat)

    def mute_notifications(self, chat: ChatRoom):
        if chat not in self.chats:
            raise Exception(f"User {self} not a member of {chat}")
        chat.notification_service.remove_user(self)

    def unmute_notifications(self, chat: ChatRoom):
        if chat not in self.chats:
            raise Exception(f"User {self} not a member of {chat}")
        chat.notification_service.add_user(self)

    def __repr__(self) -> str:
        return self.name


class ChatRoom:
    """
    ChatRoom for chats. IM and Group chats are implemented the same way
    """

    def __init__(self, name: str, user: User):
        self.name = name
        self.members: Set[User] = set()
        self.messages: list[tuple[User, str]] = []
        self.notification_service: NotificationService = NotificationService(self)
        self.add_member(user)

    def invite_friends(self, inviter: User, users: List[User]):
        for user in users:
            user.queue_chat_invite(self)

    def send_message(self, user: User, message):
        self.messages.append((user, message))
        print(f"ChatRoom {self}: {user} sent a message")
        self.notification_service.notify(user)

    def remove_member(self, user: User):
        if user not in self.members:
            raise Exception(f"{user.name} not in {self.name}")
        self.members.remove(user)
        self.notification_service.remove(user)
        print(f"ChatRoom {self}: {user} removed")

    def add_member(self, user: User):
        if user in self.members:
            raise Exception(f"{user} already member of {self}")
        self.members.add(user)
        self.notification_service.add_user(user)
        user.join_chat(self)
        print(f"ChatRoom {self}: {user} joined chat")

    def print_chat(self):
        messages = []
        for sender, message in self.messages:
            messages.append(f"{sender}: {message}")
        print("\n".join(messages))

    def __repr__(self) -> str:
        return self.name


class OnlineChatSingleton:
    """
    OnlineChat application instance
    """

    _instance = None

    def __init__(self):
        self.users: Set[User] = set()
        self.chats: Set[User] = set()

    @staticmethod
    def get_instance():
        if not OnlineChatSingleton._instance:
            OnlineChatSingleton._instance = OnlineChatSingleton()
        return OnlineChatSingleton._instance

    def create_user(self, user: User) -> None:
        self.users.add(user)

    def remove_user(self, user: User) -> None:
        if user not in self.users:
            raise Exception(f"User {user.name} not in the system")
        self.users.remove(user)

        for friend in self.users:
            if user in friend.friends:
                friend.remove_friend(user)

    def create_chat(self, chat: ChatRoom):
        self.chats.add(chat)
        print(f"OnlineChat: {chat} created")

    def remove_chat(self, chat: ChatRoom):
        if chat not in self.chats:
            raise Exception(f"{chat.name} not in OnlineChat instance")
        self.chats.remove(chat)


class NotificationService:
    """
    Implementation of the observer pattern

    NotificationService is the publisher and users are the subscribers
    """

    def __init__(self, chat):
        self.subscribers = set()
        self.chat = chat

    def notify(self, user: User):
        for sub in self.subscribers:
            if sub is user:
                continue
            print(
                f"NotificationService: {sub.name} received a message from "
                f"{user.name} in {self.chat.name}"
            )

    def add_user(self, user: User):
        if user in self.subscribers:
            raise Exception(f"{user} already subscribed")
        self.subscribers.add(user)
        print(f"NotificationService: {user} added {self.chat} Notifications")

    def remove_user(self, user: User):
        if user not in self.subscribers:
            raise Exception(f"{user} not subscribed")
        self.subscribers.remove(user)
        print(f"NotificationService: {user} removed {self.chat} Notifications")


def main():
    # create chat singleton
    online_chat = OnlineChatSingleton.get_instance()

    # create users
    user1 = User("user1")
    user2 = User("user2")
    user3 = User("user3")

    # create chat
    chat1 = ChatRoom("chat1", user1)
    online_chat.create_chat(chat1)

    print(user1.chats)

    # invite friends to chat
    chat1.invite_friends(user1, [user2, user3])
    chat1.send_message(user1, "Hello friends! Thank you for joining!")

    # accept chat invites
    user2.accept_chat_invite(chat1)
    user3.accept_chat_invite(chat1)

    # send messages
    chat1.send_message(user2, "wassap!")
    chat1.send_message(user3, "hey friends!!")

    # mute notifications
    user1.mute_notifications(chat1)

    chat1.send_message(user2, f"I think {user1} muted us!")
    chat1.send_message(user3, "I think you're right")

    # unmute notif
    user1.unmute_notifications(chat1)

    chat1.send_message(user1, "I'm back!")
    chat1.send_message(user2, "He's back!")
    chat1.send_message(user3, "heyooo!")

    # print chat
    chat1.print_chat()


if __name__ == "__main__":
    main()
