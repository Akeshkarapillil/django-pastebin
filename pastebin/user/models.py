from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    POST_TYPE = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    id = models.BigAutoField(
        verbose_name="ID",
        primary_key=True
    )

    title = models.CharField(
        verbose_name="Title",
        max_length=70,
        null=False,
        blank=False
    )

    body = models.TextField(
        verbose_name="Content",
        blank=False,
        null=False
    )

    post_type = models.CharField(
        verbose_name="Post type",
        max_length=20,
        choices=POST_TYPE
    )

    password = models.CharField(
        verbose_name="Password",
        max_length=25,
        help_text="Leave it blank to make the post public"
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )