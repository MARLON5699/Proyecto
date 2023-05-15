# Generated by Django 4.2 on 2023-05-15 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Valor total')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.persona', verbose_name='Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Precio Unitario')),
                ('cantidad_total', models.PositiveIntegerField(default=1, verbose_name='Cantidad Total')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.venta', verbose_name='Venta')),
            ],
        ),
    ]