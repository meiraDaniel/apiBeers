from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from beers.models import Beers
from beers.serializers import BeersSerializer
from beers.permissions import IsCreatorOrReadOnly

class BeerList(viewsets.ModelViewSet) :
    #Permisões que limitam a visualização da API a usuários autenticados e a edição e exclusão aos criadores daquela atividade.
    permission_classes = (IsAuthenticated, IsCreatorOrReadOnly,)
    queryset = Beers.objects.all()
    serializer_class = BeersSerializer

    #Metodo responsável por assim que uma nova atividade for criada automaticamente passa para o serializer do BeerList quem é o usuário autenticado no momento. 
    def perform_create(self, serializer):
        serializer.save(userId=self.request.user)