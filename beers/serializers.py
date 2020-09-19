from rest_framework import serializers
from beers.models import Beers

class BeersSerializer(serializers.ModelSerializer):
    #Inicializando o creator no serializer como um campo somente de leitura, e obtendo o valor do username do usuário autenticado no momento.
    userId = serializers.ReadOnlyField(source='userId.username')
    class Meta:
        model = Beers
        fields = '__all__'