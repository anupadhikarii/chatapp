# Generated by Django 4.0.1 on 2022-02-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.CharField(max_length=150)),
                ('room', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]