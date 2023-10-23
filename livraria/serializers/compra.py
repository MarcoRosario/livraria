from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from livraria.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    
    class Meta:
        model = ItensCompra
        fields = "__all__"
        depth = 1
        
    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco

class CompraSerializer(ModelSerializer):
   usuario = CharField(source="usuario.email", read_only=True)
   status = CharField(source="get_status_display", read_only=True)
   itens = ItensCompraSerializer(many=True, read_only=True)
   
   class Meta: 
        model = Compra
        fields = "__all__"
 
        

   