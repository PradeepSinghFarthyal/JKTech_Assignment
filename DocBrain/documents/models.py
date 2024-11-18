from django.db import models

# Create your models here.
class Document(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Embedding(models.Model):
    doc = models.ForeignKey(Document, on_delete=models.CASCADE)
    vector = models.JSONField()  # Use JSONField for numpy array compatibility
    created_at = models.DateTimeField(auto_now_add=True)