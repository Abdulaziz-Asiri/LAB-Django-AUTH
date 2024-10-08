# Generated by Django 4.2.14 on 2024-08-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('working_hours', models.CharField(choices=[('SunThu', 'Sunday - Thursday'), ('All', 'All Week'), ('MonFri', 'Monday - Friday')], default='SunThu', max_length=50)),
                ('feature_image', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('doctors_id', models.ManyToManyField(related_name='products', to='doctor.doctor')),
            ],
        ),
    ]
