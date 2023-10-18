# Generated by Django 4.2.6 on 2023-10-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managedsystemcpu',
            name='configurable_sys_proc_units',
            field=models.FloatField(blank=True, null=True, verbose_name='Configurable Proc Units'),
        ),
        migrations.AlterField(
            model_name='managedsystemcpu',
            name='curr_avail_sys_proc_units',
            field=models.FloatField(blank=True, null=True, verbose_name='Available Proc Units'),
        ),
        migrations.AlterField(
            model_name='managedsystemcpu',
            name='deconfig_sys_proc_units',
            field=models.FloatField(blank=True, null=True, verbose_name='Deconfigured Proc Units'),
        ),
        migrations.AlterField(
            model_name='managedsystemmemory',
            name='configurable_sys_mem',
            field=models.FloatField(blank=True, null=True, verbose_name='Configurable Memory'),
        ),
        migrations.AlterField(
            model_name='managedsystemmemory',
            name='curr_avail_sys_mem',
            field=models.FloatField(blank=True, null=True, verbose_name='Available Memory'),
        ),
        migrations.AlterField(
            model_name='managedsystemmemory',
            name='deconfig_sys_mem',
            field=models.FloatField(blank=True, null=True, verbose_name='Deconfigured Memory'),
        ),
        migrations.AlterField(
            model_name='managedsystemmemory',
            name='mem_region_size',
            field=models.FloatField(blank=True, null=True, verbose_name='Memory Region Size'),
        ),
        migrations.AlterField(
            model_name='managedsystemvm',
            name='lpar_ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='Lpar IP Address'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='desired_mem',
            field=models.FloatField(blank=True, null=True, verbose_name='Desired Memory'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='desired_proc_units',
            field=models.FloatField(blank=True, null=True, verbose_name='Desired Proc Units'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='desired_procs',
            field=models.FloatField(blank=True, null=True, verbose_name='Desired Procs'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='max_mem',
            field=models.FloatField(blank=True, null=True, verbose_name='Max Memory'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='max_proc_units',
            field=models.FloatField(blank=True, null=True, verbose_name='Max Proc Units'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='max_procs',
            field=models.FloatField(blank=True, null=True, verbose_name='Max Procs'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='mem_mode',
            field=models.FloatField(blank=True, null=True, verbose_name='Memory Mode'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='min_mem',
            field=models.FloatField(blank=True, null=True, verbose_name='Min Memory'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='min_proc_units',
            field=models.FloatField(blank=True, null=True, verbose_name='Min Proc Units'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='min_procs',
            field=models.FloatField(blank=True, null=True, verbose_name='Min Procs'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='proc_mode',
            field=models.FloatField(blank=True, null=True, verbose_name='CPU Mode'),
        ),
        migrations.AlterField(
            model_name='memorycpuvm',
            name='uncap_weight',
            field=models.FloatField(blank=True, default=128, null=True, verbose_name='Uncapped Weight'),
        ),
    ]