from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.generics import get_object_or_404



from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

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

