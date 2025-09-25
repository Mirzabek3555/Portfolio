from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    live_url = models.URLField(blank=True)
    code_url = models.URLField(blank=True)
    thumbnail = models.ImageField(upload_to='projects/', blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='projects', blank=True)
    featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.name} <{self.email}>"
