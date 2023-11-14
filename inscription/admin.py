from django.contrib import admin
from .models import InscriptionEntreprise, InscriptionAlumnus, Etudiant, Entreprise, Utilisateur

# Register your models here.
@admin.register(InscriptionEntreprise)
class InscriptionEntrepriseAdmin(admin.ModelAdmin):
    pass

@admin.register(InscriptionAlumnus)
class InscriptionEntrepriseAdmin(admin.ModelAdmin):
    pass

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    exclude = ("first_name", "last_name")

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    exclude = ("first_name", "last_name")

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    exclude = ("first_name", "last_name", "prenom")
