from asyncio import mixins
from rest_framework import generics, status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import APIException, MethodNotAllowed
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cursos import serializers

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer

"""
API V1
"""
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if (len(request.data['titulo']) <5):
            raise APIException("Titulo deve ter no mínimo 5 caracteres")
        serializer.save()
        return Response({"id":serializer.data['id'],"Curso:":serializer.data['titulo']},status=status.HTTP_201_CREATED)

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
        # self kwargs pega os valores mandados (curso_pk), no caso, conforme definido na url
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = CursoSerializer
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                    curso_id=self.kwargs.get('curso_id'),
                    pk=self.kwargs.get('avaliacao_pk'))
            return get_object_or_404(self.get_queryset(),pk=self.kwargs.get('avaliacao_pk'))

"""
API V2
"""



""" Outra forma de gerar somente métodos de interesse:
class CursoViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):

ReadOnlyModelViewSet - Manterá apenas métodos somente leitura. Que são basicamente solicitações 
"GET" e "OPTIONS".

CreateModelMixin - Isso permitirá apenas a criação de novos elementos. Qual é a solicitação "POST".

Todos os outros métodos como "PUT", "PATH" e "DELETE" estão desabilitados no exemplo acima.
Você pode habilitar vários métodos usando mixins com base em seus requisitos.
"""

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    """ Mais maneiras de não permitir algumas ações
    #http_method_names = ['get', 'post', 'head'] # para definir a penas os métodos que quero
    
    class AvaliacaoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet): #herdando somente classes de list
        queryset = Avaliacao.objects.all()
        serializer_class = AvaliacaoSerializer

    # para personalizar erro em método nao permitido
    def list(self, request):
        raise MethodNotAllowed('GET', detail='Method GET not allowed without lookup')
    """                         
    
    @action(detail=True, methods=['get']) #cursos/id/avaliacoes
    def avaliacoes(self,request,pk=None):
        """ Sem paginação 
            curso = self.get_object()
            serializer = AvaliacaoSerializer(curso.avaliacoes.all(),many=True)
            return Response(serializer.data)
        """
        """Com Paginação"""
        self.pagination_class.page_size=1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page=self.paginate_queryset(avaliacoes)
        
        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
   pagination_class = None # disable pagination configured in global
   queryset = Avaliacao.objects.all()
   serializer_class = AvaliacaoSerializer


    