# Generated by Django 5.0.6 on 2024-05-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('imagen', models.CharField(max_length=200)),
            ],
        ),
    ]