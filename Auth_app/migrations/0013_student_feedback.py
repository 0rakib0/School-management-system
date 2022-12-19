# Generated by Django 4.1.1 on 2022-11-02 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_app', '0012_student_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('reply_feedback', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth_app.student')),
            ],
        ),
    ]