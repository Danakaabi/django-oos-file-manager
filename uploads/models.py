from django.db import models

class UploadedFile(models.Model):
    original_name = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads/%Y/%m/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.original_name
