# Generated by Django 4.2.9 on 2024-01-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Breed', models.CharField(max_length=50)),
                ('Color', models.CharField(max_length=10)),
                ('DogName', models.CharField(max_length=50)),
                ('Postcode', models.CharField(max_length=10)),
            ],
        ),
    ]