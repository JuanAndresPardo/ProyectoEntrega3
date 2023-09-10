# Generated by Django 4.2.2 on 2023-09-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppStock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Transportista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='codigo',
            new_name='peso',
        ),
    ]