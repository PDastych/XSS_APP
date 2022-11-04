# Generated by Django 4.1.2 on 2022-11-03 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('stored_xss_module_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.storedxssmodule')),
            ],
        ),
    ]
