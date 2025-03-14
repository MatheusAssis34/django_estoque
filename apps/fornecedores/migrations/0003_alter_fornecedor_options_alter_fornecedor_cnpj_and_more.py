# Generated by Django 5.1.6 on 2025-02-27 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0002_alter_fornecedor_cnpj_alter_fornecedor_nome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'ordering': ['-id'], 'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(blank='False', max_length=200, null='False', unique=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='contato',
            field=models.CharField(blank='False', max_length=200, null='False', verbose_name='Contato'),
        ),
        migrations.AlterModelTable(
            name='fornecedor',
            table='fornecedor',
        ),
    ]
