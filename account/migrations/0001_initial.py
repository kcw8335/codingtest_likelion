# Generated by Django 2.1.1 on 2020-03-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
