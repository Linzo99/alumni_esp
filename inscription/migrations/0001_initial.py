# Generated by Django 4.2.1 on 2023-05-17 12:28

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Utilisateur",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("prenom", models.CharField(blank=True, max_length=150)),
                ("nom", models.CharField(max_length=150)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "utilisateur",
                "verbose_name_plural": "utilisateurs",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="InscriptionAlumnus",
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
                ("prenom", models.CharField(max_length=150)),
                ("nom", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("matricule", models.CharField(max_length=9)),
                ("cni", models.CharField(blank=True, max_length=14, null=True)),
                (
                    "departement",
                    models.CharField(
                        choices=[
                            ("informatique", "Genie Informatique"),
                            ("ELECTRIQUE", "Genie Electrique"),
                            ("mecanique", "Genie Mecanique"),
                            ("civil", "Genie Civil"),
                            ("gestion", "Gestion"),
                            ("gcba", "GCBA"),
                        ],
                        max_length=100,
                    ),
                ),
                ("telephone", models.CharField(blank=True, max_length=15, null=True)),
                ("annee_entree", models.DateField(blank=True, null=True)),
                ("annee_sortie", models.DateField(blank=True, null=True)),
                (
                    "piece_jointe",
                    models.FileField(upload_to="inscription/alumnus/%Y/%m/%d-%H:%M:%S"),
                ),
                ("creation", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="InscriptionEntreprise",
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
                ("nom", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                (
                    "localisation",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("matricule", models.CharField(blank=True, max_length=15, null=True)),
                ("description", models.TextField()),
                (
                    "piece_jointe",
                    models.FileField(
                        upload_to="inscription/entreprise/%Y/%m/%d-%H:%M:%S"
                    ),
                ),
                ("creation", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Entreprise",
            fields=[
                (
                    "utilisateur_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "localisation",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("matricule", models.CharField(blank=True, max_length=15, null=True)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("inscription.utilisateur",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Etudiant",
            fields=[
                (
                    "utilisateur_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("matricule", models.CharField(max_length=9)),
                ("cni", models.CharField(blank=True, max_length=14, null=True)),
                (
                    "departement",
                    models.CharField(
                        choices=[
                            ("informatique", "Genie Informatique"),
                            ("ELECTRIQUE", "Genie Electrique"),
                            ("mecanique", "Genie Mecanique"),
                            ("civil", "Genie Civil"),
                            ("gestion", "Gestion"),
                            ("gcba", "GCBA"),
                        ],
                        max_length=100,
                    ),
                ),
                ("telephone", models.CharField(blank=True, max_length=15, null=True)),
                ("annee_entree", models.DateField(blank=True, null=True)),
                ("is_alumnus", models.BooleanField(default=False)),
                ("annee_sortie", models.DateField(blank=True, null=True)),
                (
                    "localisation",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "diplome",
                    models.FileField(
                        blank=True,
                        upload_to="inscription/alumnus/diplome/%Y/%m/%d-%H:%M:%S",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("inscription.utilisateur",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
