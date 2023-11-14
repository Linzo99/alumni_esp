from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import *

# InscriptionAlumnus serializers
class InscriptionAlumnusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscriptionAlumnus
        exclude = ("creation", "valide")

# InscriptionEntreprise serializers
class InscriptionEntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscriptionEntreprise
        exclude = ("creation", "valide")

# Utilisateur serializer
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        exclude = ("first_name", "last_name")

# Etudiant serializer
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ("id",
                  "prenom",
                  "nom",
                  "email",
                  "matricule",
                  "cni",
                  "telephone",
                  "departement",
                  "annee_entree",
                  "annee_sortie",
                  "is_alumnus")
        read_only_fields = ("matricule", "cni", "prenom", "nom", "departement")

# Serializer to handle current student inscription
class EtudiantCurSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[RegexValidator(regex=r"^[a-zA-Z0-9_.+-]+@esp\.sn$")])
    class Meta:
        model = Etudiant
        fields = ("email",
                  "password")

# Entreprise serializer
class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ("nom",
                  "email",
                  "matricule",
                  "description",
                  "localisation")
        read_only_fields = ("matricule",)
