# Generated by Django 5.1.1 on 2024-11-21 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equatorcollege', '0003_unitregistration_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitregistration',
            name='term',
            field=models.IntegerField(blank=True),
        ),
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_type', models.CharField(max_length=20)),
                ('marks', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('unit_registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equatorcollege.unitregistration')),
            ],
        ),
    ]