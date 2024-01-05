# Generated by Django 2.0.2 on 2022-10-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_its_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rol',
            options={'verbose_name': 'Roles'},
        ),
        migrations.AlterField(
            model_name='rol',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rol',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]