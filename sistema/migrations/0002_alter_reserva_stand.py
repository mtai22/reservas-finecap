# Generated by Django 4.2.5 on 2023-09-20 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='stand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.stand'),
        ),
    ]
