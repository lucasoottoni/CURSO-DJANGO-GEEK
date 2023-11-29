from rest_framework import serializers

from .models import Avaliacao, Curso
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model



class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        extra_kwargs= {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso','nome','email','comentario',
            'avaliacao','avaliacao','criacao','ativo'
        )

class CursoSerializer(serializers.ModelSerializer):
    # Nested relationship - pode ter problemas em grande volumes de dados (de avaliações nesse caso) -  Será bacana por exemplo num OneToOne
        #avaliacoes = AvaliacaoSerializer(many=True, read_only=True) 
    
    #HyperLinked Related Field - cria um link para cada avaliação
        #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name = 'avaliacao-detail')
        
    # Primary Key Related Field - Traz lista somente com os ID's das avaliações
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id','titulo','url','criacao','ativo','avaliacoes'
        )
        


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = 'name'
        token['2'] = 'the name2'
        # ...
        return token

class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        
        usuario = get_user_model()
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': usuario.__name__})
       # data.update({'id': self.user.__id})
        # and everything else you want to send in the response
        return data