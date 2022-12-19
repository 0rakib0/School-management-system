# Generated by Django 4.1.1 on 2022-09-14 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth_app', '0003_course_sessin_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('create_att', models.DateTimeField(auto_now_add=True)),
                ('updated_att', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ciurse_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Auth_app.course')),
                ('session_year_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Auth_app.sessin_year')),
            ],
        ),
    ]
