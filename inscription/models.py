from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


class EnumDepartement(models.TextChoices):
    INFORMATIQUE = ("informatique", "Genie Informatique")
    ELECTRIQUE = ("electrique", "Genie Electrique")
    MECANIQUE = ("mecanique", "Genie Mecanique")
    CIVIL = ("civil", "Genie Civil")
    GESTION = ("gestion", "Gestion")
    GCBA = ("gcba", "GCBA")

# Create your models here.
class InscriptionAlumnus(models.Model):
    """
        Model inscription des alumni
    """
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    matricule = models.CharField(max_length=9, unique=True)
    cni = models.CharField(max_length=14, unique=True, blank=True, null=True)
    departement = models.CharField(max_length=100, choices=EnumDepartement.choices)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    annee_entree = models.DateField(blank=True, null=True)
    annee_sortie = models.DateField(blank=True, null=True)
    piece_jointe = models.FileField(upload_to="inscription/alumnus/%Y/%m/%d-%H:%M:%S")
    valide = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Inscription Alumni"

class InscriptionEntreprise(models.Model):
    """
        Model inscription des entreprises
    """
    nom = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    localisation = models.CharField(max_length=150, blank=True, null=True)
    matricule = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField()
    piece_jointe = models.FileField(upload_to="inscription/entreprise/%Y/%m/%d-%H:%M:%S")
    valide = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)


##########################################
# USERS MODELS HERE
##########################################
class Utilisateur(AbstractUser):
    """
        Model Utilisateur de base
    """
    prenom = models.CharField(max_length=150, blank=True)
    nom = models.CharField(max_length=150)
    email = models.EmailField(blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "utilisateur"
        verbose_name_plural = "utilisateurs"
        abstract = False

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.prenom, self.nom)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.prenom

class Etudiant(Utilisateur, models.Model):
    """
        Model Etudiant
    """
    matricule = models.CharField(max_length=9)
    cni = models.CharField(max_length=14, blank=True, null=True)
    departement = models.CharField(max_length=100, choices=EnumDepartement.choices)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    annee_entree = models.DateField(blank=True, null=True)
    # la nationalite
    # les attributs d'un alumnus
    is_alumnus = models.BooleanField(default=False)
    annee_sortie = models.DateField(blank=True, null=True)
    localisation = models.CharField(max_length=150, blank=True, null=True)
    diplome = models.FileField(upload_to="inscription/alumnus/diplome/%Y/%m/%d-%H:%M:%S", blank=True)

    class Meta:
        verbose_name = "etudiant"
        verbose_name_plural = "etudiants"

class Entreprise(Utilisateur):
    """
        Model Entreprise
    """
    localisation = models.CharField(max_length=150, blank=True, null=True)
    matricule = models.CharField(max_length=15, blank=True, null=True) # Ninea
    description = models.TextField()

    class Meta:
        verbose_name = "entreprise"
        verbose_name_plural = "entreprises"
