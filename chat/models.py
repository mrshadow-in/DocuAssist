from django.db import models
from users.models import CustomUser  # Import the CustomUser model from the users app


class ChatMessage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to='chat/images/', blank=True, null=True)  # Add image field
    comment = models.TextField(blank=True, null=True)  # Add comment field
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.timestamp}"
