# Generated by Django 3.0.1 on 2020-03-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_login_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, default='Unnamed User', max_length=30, verbose_name='first name'),
        ),
    ]
