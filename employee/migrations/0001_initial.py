# Generated by Django 2.2.2 on 2023-04-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUserEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Driver_name', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255, unique=True)),
                ('NID', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('license_no', models.TextField()),
                ('license_renewed', models.DateTimeField()),
                ('specialization', models.TextField()),
                ('experience', models.TextField()),
                ('address', models.TextField()),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('vehicle_id', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
