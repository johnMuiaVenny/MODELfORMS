# Generated by Django 3.2.5 on 2021-07-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COMMENTT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.FileField(upload_to='images')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
    ]