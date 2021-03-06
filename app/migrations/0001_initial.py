# Generated by Django 3.1 on 2020-08-31 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('bebe', models.BooleanField(verbose_name='Bebe?')),
                ('tipo', models.IntegerField(choices=[(1, 'Funcionário'), (2, 'Convidado')], verbose_name='Tipo de pessoa')),
                ('valor_pagar', models.FloatField(verbose_name='Valor a pagar')),
                ('convidado', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pessoa', verbose_name='Convidado')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ('nome',),
            },
        ),
    ]
