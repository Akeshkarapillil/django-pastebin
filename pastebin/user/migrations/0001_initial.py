# Generated by Django 3.0.8 on 2020-09-30 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Content')),
                ('post_type', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=20, verbose_name='Post type')),
                ('password', models.CharField(help_text='Leave it blank to make the post public', max_length=25, verbose_name='Password')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]