# Generated by Django 3.2 on 2022-10-17 18:35

from django.db import migrations, models
import pandas as pd

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_its_staff'),
    ]

    def insert_initial_data(apps, schema_editor):
        #read csv file
        df = pd.read_csv('users/migrations/roles.csv')

        arr_rols = df['nombre'].unique()

        Rol = apps.get_model('users', 'Rol')

        for i in arr_rols:
            Rol.objects.create(name=i)


    def undo_insert_data(apps, schema_editor):
        Rol = apps.get_model('users', 'Rol')
        Rol.objects.all().delete()

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RunPython(insert_initial_data, reverse_code=undo_insert_data)
    ]