# Generated by Django 4.1.4 on 2023-01-01 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transport_orders', '0002_alter_transportorder_transport'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportOrderArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_quantity', models.PositiveIntegerField()),
                ('transport_quantity', models.PositiveIntegerField()),
                ('reason', models.TextField(null=True)),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Added')], default='1', max_length=2)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('transport_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport_orders.transportorder')),
            ],
        ),
    ]
