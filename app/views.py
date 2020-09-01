
from django.http import Http404, HttpResponse
from django.shortcuts import render

from rest_framework import generics, status, views
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.

# PESSOA ==========================================================================================================================

class ParticiparChurrasco(generics.CreateAPIView):

    serializer_class = FuncionarioSerializer

class ShowFuncionarios(generics.ListAPIView):

    queryset = Pessoa.objects.filter(tipo=1)
    serializer_class = FuncionarioShowSerializer

class ShowConvidados(generics.ListAPIView):

    queryset = Pessoa.objects.filter(tipo=2)
    serializer_class = ConvidadoShowSerializer

class CancelarParticipacao(generics.DestroyAPIView):

    queryset = Pessoa.objects.all()
    serializer_class = PessoaDeleteSerializer

    def delete(self, request, pk):
        pessoa = self.get_object()
        
        if (pessoa.tipo == 1):
            if not (pessoa.convidado == None):
                pessoa.convidado.delete()
            pessoa.delete()
        else:
            bebe = pessoa.bebe
            funcionario = Pessoa.objects.filter(convidado=pessoa)[0]

            pessoa.delete()

            funcionario.convidado = None
            funcionario.valor_pagar -= 20 if bebe else 10
            funcionario.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class TotalArrecadado(views.APIView):

    def get(self, request):
        total = 0

        for func in Pessoa.objects.filter(tipo=1):
            total += func.valor_pagar
        data = {'total_arrecadado': total}

        return Response(data, status=status.HTTP_200_OK)

# COMPRA ========================================================================================================================

class CompraView(generics.ListCreateAPIView):

    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Compra.objects.all()
    serializer_class = CompraDetailSerializer

    def put(self, request, pk):
        compra = self.get_object()
        data = request.data
        data['preco_total'] = data['preco_unitario'] * data['qtd']
        serializer = CompraDetailSerializer(compra, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TotalGastoCompra(views.APIView):

    def get(self, request):
        COMPRA_CODE = {'comida': 1, 'bebida': 2}

        tipo_total = request.path.split('/')[-2]

        total = 0
        if tipo_total == 'total-compras':
            key = 'total_gasto'
            for compra in Compra.objects.all():
                total += compra.preco_total
        else:
            key = 'total_gasto_' + tipo_total
            for compra in Compra.objects.filter(tipo=COMPRA_CODE[tipo_total]):
                total += compra.preco_total
        
        data = {key: total}
        return Response(data, status=status.HTTP_200_OK)