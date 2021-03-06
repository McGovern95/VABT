# Generated by Django 2.1.7 on 2019-04-02 02:33

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190401_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextended',
            name='cert_of_elig',
            field=models.FileField(blank=True, default=django.utils.timezone.now, upload_to='profile_pics', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
            preserve_default=False,
        ),
    ]
