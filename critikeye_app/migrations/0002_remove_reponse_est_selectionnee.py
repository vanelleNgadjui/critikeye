# Generated by Django 4.2.2 on 2023-06-22 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('critikeye_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reponse',
            name='est_selectionnee',
        ),
    ]
