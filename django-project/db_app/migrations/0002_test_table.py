# Generated by Django 4.2.5 on 2023-10-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
