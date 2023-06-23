# Generated by Django 4.2.2 on 2023-06-23 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('critikeye_app', '0002_remove_reponse_est_selectionnee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technophile',
            name='technophile_name',
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='groups',
            field=models.ManyToManyField(related_name='entreprise_users', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='user_permissions',
            field=models.ManyToManyField(related_name='entreprise_users', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='technophile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]