# Generated by Django 4.1.7 on 2023-03-09 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_tag_delete_tags_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
