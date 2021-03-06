# Generated by Django 3.2.6 on 2021-09-01 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=8, unique=True)),
                ('host', models.CharField(max_length=50, unique=True)),
                ('skipVotes', models.IntegerField(default=1)),
                ('canPause', models.BooleanField(default=False)),
                ('timeCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
