# Generated by Django 4.2.6 on 2023-10-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.FileField(default=None, null=True, upload_to='user_app/'),
        ),
    ]
