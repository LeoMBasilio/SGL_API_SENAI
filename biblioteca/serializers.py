from .models import Livros, usuarios, locacao
from rest_framework import serializers
from .validators import validate_celular,validate_cpf,validate_email,validate_nome, validate_quantidade_negativa, validate_quantidade_em_estoque

class LivrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'
        
    def validate(self, data):
        if not validate_nome(data['autor']):
            raise serializers.ValidationError(
                'O nome do autor nao corresponde ao esperado'
            )
        if validate_quantidade_negativa(data['quantidade']):
            raise serializers.ValidationError(
                'A quantidade de livros nao pode ser negativa'
            )
        return data
    
class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ['id', 'nome', 'cpf', 'email', 'celular', 'endereco']

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
        fields = ['id', 'usuario', 'livro', 'data_locacao', 'data_devolucao', 'devolvido']
        read_only_fields = ['usuario', 'data_locacao']

    def validate(self, data):
        if validate_quantidade_em_estoque(data['livro'].quantidade):
            raise serializers.ValidationError(
                'Nao ha livros disponiveis para locacao'
            )
        return data
    
    def create(self, validated_data):
        livro = validated_data['livro']
        livro.quantidade -= 1
        livro.save()
        validated_data['usuario'] = usuarios.objects.get(user=self.context['request'].user)
        return super().create(validated_data)