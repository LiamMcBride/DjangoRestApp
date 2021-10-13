# Generated by Django 3.2.8 on 2021-10-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('countryId', models.IntegerField()),
            ],
        ),
    ]
