# Generated by Django 2.2.10 on 2020-02-14 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmueble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=10, max_digits=10)),
                ('alcoba', models.IntegerField()),
                ('baño', models.IntegerField()),
                ('parqueadero', models.BooleanField()),
                ('disponible', models.BooleanField()),
                ('IDBarrio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inmueble.Barrio')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_de_inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_de_oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Tipo_Inmueble',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='IDTipo_de_inmueble',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inmueble.Tipo_de_inmueble'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='IDTipo_de_oferta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inmueble.Tipo_de_oferta'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='IDDepartamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inmueble.Departamento'),
        ),
        migrations.AddField(
            model_name='barrio',
            name='IDCiudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inmueble.Ciudad'),
        ),
    ]
