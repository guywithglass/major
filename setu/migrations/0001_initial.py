# Generated by Django 5.1.3 on 2024-11-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('crop', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
