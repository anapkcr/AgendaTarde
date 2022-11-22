# Generated by Django 4.1.3 on 2022-11-22 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0001_initial'),
        ('servico', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField(help_text='Data e hora do atendimento', verbose_name='Horário')),
                ('situacao', models.CharField(choices=[('A', 'Agendado'), ('B', 'Realizado'), ('C', 'Cancelado')], default='A', help_text='Situação do atendimento', max_length=15, verbose_name='Situação')),
                ('cliente', models.ForeignKey(help_text='Nome do cliente', on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Cliente')),
                ('funcionario', models.ForeignKey(help_text='Nome do funcionario', on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario', verbose_name='Funcionario')),
                ('servico', models.ForeignKey(help_text='Nome do serviço', on_delete=django.db.models.deletion.CASCADE, to='servico.servico', verbose_name='Serviço')),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
            },
        ),
    ]