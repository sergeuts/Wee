# Generated by Django 4.1.2 on 2022-10-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='registration_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Registration date'),
        ),
    ]