# Generated by Django 4.1.1 on 2022-09-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_app', '0002_rename_user_profile_pic_customuser_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('created_att', models.DateTimeField(auto_now_add=True)),
                ('updated_att', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sessin_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.CharField(max_length=100)),
                ('session_end', models.CharField(max_length=100)),
            ],
        ),
    ]