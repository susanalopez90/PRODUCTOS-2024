# Generated by Django 5.1.1 on 2024-10-08 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('ProductoId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Nombre', models.TextField(max_length=50)),
                ('Descripcion', models.TextField(max_length=250)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=12)),
                ('Cantidad', models.IntegerField()),
                ('Estado', models.FloatField()),
            ],
        ),
    ]