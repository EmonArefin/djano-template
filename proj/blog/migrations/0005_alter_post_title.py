# Generated by Django 4.1.7 on 2023-03-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Enter Your Title', max_length=200, null=True),
        ),
    ]
