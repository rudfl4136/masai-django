# Generated by Django 5.1.7 on 2025-03-25 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AiWorkedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gubun', models.CharField(max_length=100)),
                ('request_contents', models.CharField(max_length=2000)),
                ('request_worked_date', models.DateTimeField(verbose_name='date published')),
                ('response_contents', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='BlogKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thema', models.CharField(max_length=1000)),
                ('category', models.CharField(max_length=1000)),
                ('worked_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
