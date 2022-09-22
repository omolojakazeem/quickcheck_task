from django.contrib.postgres.fields import ArrayField
from django.db import models


NEWS_TYPE = (
    ("JOB", "JOB"),
    ("COMMENT", "COMMENT"),
    ("STORY", "STORY"),
    ("POLL", "POLL"),
    ("POLLOPT", "POLLOPT"),
)


class News(models.Model):
    """
    Model: News
    Database Table to hold News instances
    """
    s_n = models.BigIntegerField(unique=True, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    type = models.CharField(max_length=7, choices=NEWS_TYPE, null=True, blank=True)
    by = models.CharField(max_length=255, null=True, blank=True)
    time = models.IntegerField(null=True, blank=True)
    dead = models.BooleanField(default=False)
    kids = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    parts = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    descendants = models.IntegerField(null=True, blank=True)
    parent = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    synced = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added']

    def __str__(self):
        if self.title:
            return f"News Item - {self.title} (Type - {self.type})"
        else:
            return f"News Item - {self.pk} (Type - {self.type})"
