from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import DjangoModelPermissionsOrAnonCreate

from django.forms.models import model_to_dict

from .models import *
from .serializers import *

# Create your views here

EXCLUDE = ('valide', 'piece_jointe')

class InscriptionEtudiant(CreateAPIView):
    "view pour inscription d'un etudiant actuel"
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantCurSerializer

class InscriptionAlumnusViewSet(ModelViewSet):
    "ViewSet pour InscriptionAlumnus"
    queryset = InscriptionAlumnus.objects.all()
    serializer_class = InscriptionAlumnusSerializer
    permission_classes = [DjangoModelPermissionsOrAnonCreate]

    @action(detail=True, methods=['post'])
    def validate(self, request, pk):
        """Valider une demande d'inscription alumnus"""
        instance = self.get_object()
        demande = model_to_dict(instance, exclude=['piece_jointe', 'valide'])
        alumnus = Etudiant.objects.create(**demande)
        instance.valide = True
        instance.save(update_fields=('valide',))
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

class InscriptionEntrepriseViewSet(ModelViewSet):
    "ViewSet pour InscriptionEntreprise"
    queryset = InscriptionEntreprise.objects.all()
    serializer_class = InscriptionEntrepriseSerializer
    permission_classes = [DjangoModelPermissionsOrAnonCreate]

    @action(detail=True, methods=['post'])
    def validate(self, request, pk):
        """Valider une demande d'inscription entreprise"""
        instance = self.get_object()
        demande = model_to_dict(instance, exclude=['piece_jointe', 'valide'])
        entreprise = Entreprise.objects.create(**demande)
        instance.valide = True
        instance.save(update_fields=('valide',))
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

class UtilisateurViewSet(ModelViewSet):
    "ViewSet pour Utilisateur"
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [DjangoModelPermissions]

class EtudiantViewSet(ModelViewSet):
    "ViewSet pour Etudiant"
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = [DjangoModelPermissions]

class EntrepriseViewSet(ModelViewSet):
    "ViewSet pour Entreprise"
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    permission_classes = [DjangoModelPermissions]
