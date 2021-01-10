from django.db import models
from django.conf import settings


class Notes(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=264, verbose_name="Put a Title")
    body = models.TextField()
    shared = models.BooleanField(default=False)
    shared_with = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="shared_users")
    publish_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_date', ]

    def __str__(self):
        return self.title
