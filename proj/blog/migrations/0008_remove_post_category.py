# Generated by Django 4.1.7 on 2023-03-06 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]