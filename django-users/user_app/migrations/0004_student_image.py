# Generated by Django 4.2.5 on 2023-10-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_remove_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.FileField(null=True, upload_to='users/'),
        ),
    ]