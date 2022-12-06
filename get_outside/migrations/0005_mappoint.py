# Generated by Django 4.1.3 on 2022-12-01 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('get_outside', '0004_delete_mappoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mappoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('notes', models.CharField(choices=[('Outdoor', 'Outdoor Activity'), ('Indoor', 'Indoor Activity'), ('Out & In', 'Outdoor and Indoor Activity')], default='Outdoor', max_length=100)),
                ('openingHours', models.DateTimeField()),
                ('description', models.TextField()),
                ('picture', models.TextField()),
                ('longitude', models.FloatField(max_length=10)),
                ('latitude', models.FloatField(max_length=10)),
                ('ratings', models.FloatField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='get_outside.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
