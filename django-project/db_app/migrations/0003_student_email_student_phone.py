# Generated by Django 4.2.5 on 2023-10-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0002_test_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
