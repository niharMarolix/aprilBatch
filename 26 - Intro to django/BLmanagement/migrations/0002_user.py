# Generated by Django 4.2.6 on 2023-10-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BLmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]