from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import APIException


from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer


class CursoAPIView(APIView):
    """
    API DE Cursos
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if (len(request.data['titulo']) <5):
            raise APIException("Titulo deve ter no mínimo 5 caracteres")
        serializer.save()
        # return Response(serializer.data,status=status.HTTP_201_CREATED)
        # return Response({"msg":"Curso criado!"},status=status.HTTP_201_CREATED)
        return Response({"id":serializer.data['id'],"Curso:":serializer.data['titulo']},status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """
    API DE Avaliações 
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    