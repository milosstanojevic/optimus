# Generated by Django 4.1.4 on 2023-01-01 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouses', '0001_initial'),
        ('regals', '0001_initial'),
        ('regal_positions', '0002_initial'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('regal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regals.regal')),
                ('regal_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regal_positions.regalposition')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouses.warehouse')),
            ],
        ),
    ]
