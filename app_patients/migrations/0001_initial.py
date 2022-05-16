# Generated by Django 4.0.4 on 2022-05-15 07:54

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('is_patient', models.BooleanField(default=True)),
                ('card_number', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'patient',
                'verbose_name_plural': 'patients',
                'db_table': 'patients',
            },
            bases=('app_users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
