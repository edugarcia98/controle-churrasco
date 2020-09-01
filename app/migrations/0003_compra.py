# Generated by Django 3.1 on 2020-09-01 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200831_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=150, verbose_name='Descrição')),
                ('tipo', models.IntegerField(choices=[(1, 'Comida'), (2, 'Bebida')], verbose_name='Tipo de compra')),
                ('preco_unitario', models.FloatField(verbose_name='Preço unitário')),
                ('qtd', models.IntegerField(verbose_name='Quantidade')),
                ('preco_total', models.FloatField(verbose_name='Preço total')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ('desc',),
            },
        ),
    ]
