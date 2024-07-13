# Generated by Django 5.0.6 on 2024-07-13 20:36

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCGPAGE', '0005_productosglobales'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2024, 7, 13, 16, 34, 39, 893676))),
                ('total', models.IntegerField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ProductoMagic',
        ),
        migrations.DeleteModel(
            name='ProductoMYL',
        ),
        migrations.DeleteModel(
            name='ProductoPoke',
        ),
        migrations.DeleteModel(
            name='ProductoYugi',
        ),
        migrations.AddField(
            model_name='productosglobales',
            name='stack',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalle',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TCGPAGE.productosglobales'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TCGPAGE.venta'),
        ),
    ]
