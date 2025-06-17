from .models import Livros, usuarios, locacao
from rest_framework import serializers
from .validators import validate_celular,validate_cpf,validate_email,validate_nome

class LivrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'
        
    def validate(self, data):
        if not validate_nome(data['autor']):
            raise serializers.ValidationError(
                'O nome do autor nao corresponde ao esperado'
            )
        return data
    
class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = '__all__'

    def validate(self, data):
        if not validate_nome(data['nome']):
            raise serializers.ValidationError(
                'O nome de usuario nao corresponde ao esperado'
            )
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError(
                'CPF invalido'
            )
        if not validate_email(data['email']):
            raise serializers.ValidationError(
                'email invalido'
            )
        if not validate_celular(data['celular']):
            raise serializers.ValidationError(
                'numero de telefone invalido'
            )
        return data

class LocacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = locacao
        fields = '__all__'  