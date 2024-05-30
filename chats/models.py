from django.db import models

from .utils import get_random_string

import hashlib

class Chat(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name = "chats")
    timestamp = models.DateField(auto_now_add=True)
    hash = models.CharField(unique = True, default = None, null = True, blank = True, max_length = 64)

    def __str__(self):
        return f"{self.user}'s chat"

    def save(self, *args, **kwargs):
        if self.hash is None:
            raw_hash = get_random_string()
            encoded_raw_hash = raw_hash.encode()
            self.hash = hashlib.sha256(encoded_raw_hash).hexdigest()
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name = "messages")
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    from_ai = models.BooleanField(default = True)

    def __str__(self):
        return f"{self.chat} message. FROM AI - {self.from_ai}"
    