from django.db import models

class Chat(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name = "chats")
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s chat"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name = "messages")
    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat} message"
    