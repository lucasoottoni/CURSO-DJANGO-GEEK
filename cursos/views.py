from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer


class CursoAPIView(APIView):
    """
    API DE CURSOS DA GEEK
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

class AvaliacaoAPIView(APIView):
    """
    API DE Avaliações DA GEEK
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)