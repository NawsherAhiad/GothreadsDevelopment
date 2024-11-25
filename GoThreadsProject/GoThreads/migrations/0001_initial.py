# Generated by Django 4.1.5 on 2024-11-07 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_id", models.CharField(max_length=20)),
                ("company_name", models.CharField(max_length=100)),
                (
                    "company_type",
                    models.CharField(
                        choices=[
                            ("CarCompany", "Car Company"),
                            ("HotelCompany", "Hotel Company"),
                            ("MedicalCompany", "Medical Company"),
                            ("LifestyleCompany", "Lifestyle Company"),
                            ("OnlineCoursesCompany", "Online Courses"),
                            ("BabyCareCompany", "Baby Care Company"),
                            ("ServicesCompany", "Services Company"),
                            ("AirCompany", "Air Company"),
                            ("BusCompany", "Bus Company"),
                            ("LonchCompany", "Lonch Company"),
                            ("ResortCompany", "Resort Company"),
                            ("ShoppingCompany", "Shopping Company"),
                        ],
                        max_length=20,
                    ),
                ),
                ("details", models.TextField(blank=True, max_length=300)),
                ("location", models.CharField(max_length=200)),
                ("rating", models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="AirCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("price_range", models.CharField(max_length=50)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="AirLogo"),
                ),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="BabyCareCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("open_time", models.TimeField(blank=True, null=True)),
                ("close_time", models.TimeField(blank=True, null=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="BabyCareLogo"),
                ),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="BusCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("price_range", models.CharField(max_length=50)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="BusLogo"),
                ),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="CarCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="CarCompanyLogo"
                    ),
                ),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="HotelCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("room_count", models.IntegerField()),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="HotelLogo"),
                ),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="LifestyleCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("open_time", models.TimeField(blank=True, null=True)),
                ("close_time", models.TimeField(blank=True, null=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="LifestyleLogo"),
                ),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="MedicalCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("open_time", models.TimeField(blank=True, null=True)),
                ("close_time", models.TimeField(blank=True, null=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="MedicalLogo"),
                ),
                ("phone", models.CharField(max_length=15)),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="OnlineCoursesCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("price_range", models.CharField(max_length=50)),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="OnlineCourseLogo"
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="ResortCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("price_range", models.CharField(max_length=50)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="ResortLogo"),
                ),
                ("phone", models.CharField(max_length=15)),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="ServicesCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("types", models.CharField(max_length=50)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="ServiceLogo"),
                ),
                ("phone", models.CharField(max_length=15)),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="ShoppingCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("open_time", models.TimeField(blank=True, null=True)),
                ("close_time", models.TimeField(blank=True, null=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="ShoppingLogo"),
                ),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="TrainCompany",
            fields=[
                (
                    "company_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="GoThreads.company",
                    ),
                ),
                ("phone", models.CharField(max_length=15)),
                ("price_range", models.CharField(max_length=50)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="TrainLogo"),
                ),
            ],
            bases=("GoThreads.company",),
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_model", models.CharField(max_length=100)),
                ("year_of_manufacture", models.IntegerField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "car_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicles",
                        to="GoThreads.carcompany",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("doctor_name", models.CharField(max_length=100)),
                ("speciality", models.CharField(max_length=50)),
                ("education", models.CharField(blank=True, max_length=200, null=True)),
                ("rating", models.PositiveIntegerField(blank=True, null=True)),
                ("visit_price", models.PositiveIntegerField()),
                ("phone", models.CharField(max_length=15)),
                (
                    "medical_company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctors",
                        to="GoThreads.medicalcompany",
                    ),
                ),
            ],
        ),
    ]