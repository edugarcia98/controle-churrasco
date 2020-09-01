from rest_framework import serializers
from rest_framework.response import Response

from .models import Pessoa, Compra

class YesNoField(serializers.Field):

    def to_representation(self, value):
        return "Sim" if value.bebe else "Não"
    
    def to_internal_value(self, data):
        return "Sim" if data['bebe'] else "Não"

# PESSOA ==========================================================================================================================

class ConvidadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'bebe']
    
    def save(self):
        convidado = Pessoa(
            nome=self.validated_data['nome'],
            bebe=self.validated_data['bebe'],
            tipo=2,
            convidado=None,
            valor_pagar=0
        )
        
        convidado.save()
        return convidado

class FuncionarioSerializer(serializers.ModelSerializer):

    convidado = ConvidadoSerializer(allow_null=True)

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'bebe', 'convidado']
    
    def save(self):
        convidado = None

        funcionario = Pessoa(
            nome=self.validated_data['nome'],
            bebe=self.validated_data['bebe'],
            tipo=1,
            convidado=None,
            valor_pagar=0
        )

        valor_pagar = 20 if self.validated_data['bebe'] else 10
        if not (self.validated_data['convidado'] == None):
            valor_pagar += 20 if self.validated_data['convidado']['bebe'] else 10
            convidadoSerializer = ConvidadoSerializer(data=self.validated_data['convidado'])
            if convidadoSerializer.is_valid():
                convidado = convidadoSerializer.save()
        
        funcionario.convidado = convidado
        funcionario.valor_pagar = valor_pagar

        funcionario.save()
        return funcionario

class FuncionarioShowSerializer(serializers.ModelSerializer):

    bebe_desc = YesNoField(source="*")

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'bebe_desc', 'valor_pagar']

class ConvidadoShowSerializer(serializers.ModelSerializer):

    bebe_desc = YesNoField(source="*")

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'bebe_desc']

class PessoaDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = '__all__'

# COMPRA ========================================================================================================================

class CompraSerializer(serializers.ModelSerializer):

    preco_total = serializers.FloatField(read_only=True)

    class Meta:
        model = Compra
        fields = ['id', 'desc', 'tipo', 'preco_unitario', 'qtd', 'preco_total']
    
    def save(self):
        compra = Compra(
            desc=self.validated_data['desc'],
            tipo=self.validated_data['tipo'],
            preco_unitario=self.validated_data['preco_unitario'],
            qtd=self.validated_data['qtd'],
            preco_total=(self.validated_data['preco_unitario'] * self.validated_data['qtd'])
        )

        compra.save()
        return compra

class CompraDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compra
        fields = ['id', 'desc', 'tipo', 'preco_unitario', 'qtd', 'preco_total']
