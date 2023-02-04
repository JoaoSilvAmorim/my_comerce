# Generated by Django 3.2.13 on 2022-12-25 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221224_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.client'),
        ),
    ]