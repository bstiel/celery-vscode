# Generated by Django 4.1.7 on 2023-03-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1024)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'url',
            },
        ),
    ]
