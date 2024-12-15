# Generated by Django 5.0.8 on 2024-12-02 13:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlledAxle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название управляемого моста')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание управляемого моста')),
            ],
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название двигателя')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание двигателя')),
            ],
        ),
        migrations.CreateModel(
            name='FailureNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название узла отказа')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание узла отказа')),
            ],
        ),
        migrations.CreateModel(
            name='LeadingAxle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название ведущего моста')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание ведущего моста')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationMent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название организации')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание организации')),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название способа восстановления')),
                ('description', models.TextField(max_length=100, verbose_name='Описание способа восстановления')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название сервисной компании')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание сервисной компании')),
            ],
        ),
        migrations.CreateModel(
            name='TechModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название техники')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание техники')),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название трансмиссии')),
                ('description', models.TextField(max_length=100, verbose_name='Описание трансмиссии')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название ТО')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание ТО')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_no', models.CharField(max_length=100, unique=True, verbose_name='Зав. № машины')),
                ('engine_no', models.CharField(max_length=100, verbose_name='Зав. № двигателя')),
                ('transmission_no', models.CharField(max_length=100, verbose_name='Зав. № трансмиссии')),
                ('leading_axle_no', models.CharField(max_length=100, verbose_name='Зав. № ведущего моста')),
                ('controlled_axle_no', models.CharField(max_length=100, verbose_name='Зав. № управляемого моста')),
                ('supply_contract', models.CharField(max_length=200, verbose_name='Договор поставки №, дата')),
                ('shipment_date', models.DateField(verbose_name='Дата отгрузки с завода')),
                ('consignee', models.CharField(max_length=200, verbose_name='Грузополучатель (конечный потребитель)')),
                ('delivery_address', models.CharField(max_length=200, verbose_name='Адрес поставки (эксплуатации)')),
                ('eqiupment', models.CharField(max_length=200, verbose_name='Комплектация (доп. опции)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('controlled_axle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.controlledaxle', verbose_name='Модель управляемого моста')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.enginemodel', verbose_name='Модель двигателя')),
                ('leading_axle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.leadingaxle', verbose_name='Модель ведущего моста')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany', verbose_name='Сервисная компания')),
                ('tech_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.techmodel', verbose_name='Модель техники')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.transmissionmodel', verbose_name='Модель трансмиссии')),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_refusal', models.DateField(verbose_name='Дата отказа')),
                ('operating_time', models.IntegerField(verbose_name='Нароботка, м/час')),
                ('failure_desc', models.CharField(max_length=100, verbose_name='Описание отказа')),
                ('spare_parts', models.CharField(max_length=100, verbose_name='Используемые запасные части')),
                ('date_restoration', models.DateField(verbose_name='Дата восстановления')),
                ('car_downtime', models.IntegerField(default=0, verbose_name='Время простоя техники')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.car', verbose_name='Машина')),
                ('failure_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.failurenode', verbose_name='Узел отказа')),
                ('recovery_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.recoverymethod', verbose_name='Способ восстановления')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany', verbose_name='Сервисная компания')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата проведения ТО')),
                ('operating_time', models.IntegerField(verbose_name='Нароботка, м/час')),
                ('work_order_number', models.CharField(max_length=100, verbose_name='№ заказ-наряда')),
                ('work_order_date', models.DateField(verbose_name='Дата заказ-наряда')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.car', verbose_name='Машина')),
                ('organization_maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.organizationment', verbose_name='Организация, проводившая ТО')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.servicecompany', verbose_name='Сервисная компания')),
                ('type_maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silant.typemaintenance', verbose_name='Вид ТО')),
            ],
        ),
    ]
