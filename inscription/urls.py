from django.urls import path
from rest_framework import routers
from .views import (
    InscriptionEtudiant,
    InscriptionAlumnusViewSet,
    InscriptionEntrepriseViewSet,
    UtilisateurViewSet,
    EtudiantViewSet,
    EntrepriseViewSet,
)

router = routers.SimpleRouter()

router.register(r"inscriptions/alumnus", InscriptionAlumnusViewSet)
router.register(r"inscriptions/entreprise", InscriptionEntrepriseViewSet)
router.register(r"utilisateurs", UtilisateurViewSet, basename="utilisateur")
router.register(r"etudiants", EtudiantViewSet, basename="etudiant")
router.register(r"entreprises", EntrepriseViewSet, basename="entreprise")

urlpatterns = [
    *router.urls,
    path(r"inscriptions/etudiant", InscriptionEtudiant.as_view())
]
