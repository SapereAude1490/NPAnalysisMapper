# Generated by Django 4.2.6 on 2023-10-25 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_experiment_csv_files_experiment_csv_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='csv_files',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.csvfile'),
        ),
    ]