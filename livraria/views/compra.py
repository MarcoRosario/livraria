from rest_framework.viewsets import ModelViewSet

from livraria.models import Compra
from livraria.serializers import CompraSerializer, CriarEditarCompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    filterset_fields = ["usuario", "status", "data"]
    ordering_fields = ["usuario", "status", "data"]
    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)
    serializer_class = CompraSerializer
    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarCompraSerializer
        return CompraSerializer
