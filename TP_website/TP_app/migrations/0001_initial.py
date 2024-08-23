# Generated by Django 4.2.15 on 2024-08-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('eventdate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(default='', max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('graduation', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('profile', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(default='', max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=200)),
                ('event', models.CharField(max_length=20)),
            ],
        ),
    ]
