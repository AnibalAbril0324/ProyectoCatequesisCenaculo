# Generated by Django 5.0.1 on 2024-05-26 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catequesis', '0008_alter_persona_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='grupo',
            field=models.ManyToManyField(blank=True, related_name='Grupo', to='Catequesis.grupo'),
        ),
    ]
