# Generated by Django 3.2 on 2022-10-17 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20221017_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='its_staff',
            field=models.BooleanField(default=False),
        ),
    ]
