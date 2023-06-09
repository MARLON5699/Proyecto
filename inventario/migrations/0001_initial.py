# Generated by Django 4.2 on 2023-05-15 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venta', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Productos')),
            ],
            options={
                'verbose_name_plural': 'Detalle Producto',
            },
        ),
        migrations.CreateModel(
            name='Materia_Prima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el Nombre de la Materia Prima', max_length=20, verbose_name='Nombre de la Materia Prima')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo de Materia Prima')),
                ('color', models.CharField(max_length=20, verbose_name='Color Materia Prima')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Materia Prima',
            },
        ),
        migrations.CreateModel(
            name='Stock_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad Total')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('detalle_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.detalle_producto', verbose_name='Detalle Producto')),
                ('detalle_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.detalle_venta', verbose_name='Detalle venta')),
            ],
            options={
                'verbose_name_plural': 'Stock Producto',
            },
        ),
        migrations.CreateModel(
            name='Stock_Materia_Prima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de materia prima en stock')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('materia_prima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.materia_prima', verbose_name='Materia Prima')),
            ],
            options={
                'verbose_name_plural': 'Stock Materia Prima',
            },
        ),
        migrations.AddField(
            model_name='detalle_producto',
            name='stock_materia_prima',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.stock_materia_prima', verbose_name='Stock Materia Prima'),
        ),
    ]
