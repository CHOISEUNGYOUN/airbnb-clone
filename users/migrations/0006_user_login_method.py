# Generated by Django 3.0.1 on 2020-03-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200306_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('Email', 'Email'), ('Github', 'Github'), ('Kakao', 'Kakao')], default='Email', max_length=50),
        ),
    ]
