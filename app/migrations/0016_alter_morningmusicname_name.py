# Generated by Django 4.2.1 on 2023-05-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_morningmusicname_names_morningmusicname_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morningmusicname',
            name='name',
            field=models.TextField(default=''),
        ),
    ]