# Generated by Django 2.1.7 on 2019-04-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_coe', models.BooleanField(default=False)),
                ('form_info', models.BooleanField(default=False)),
                ('form_resp', models.BooleanField(default=False)),
                ('form_resident', models.BooleanField(default=False)),
                ('form_concise', models.BooleanField(default=False)),
                ('form_starda', models.BooleanField(default=False)),
            ],
        ),
    ]
