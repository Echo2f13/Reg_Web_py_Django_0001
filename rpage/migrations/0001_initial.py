# Generated by Django 4.2.1 on 2023-05-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=35)),
                ('gender', models.CharField(max_length=6)),
                ('phone_num', models.IntegerField(max_length=255)),
            ],
        ),
    ]
