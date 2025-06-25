link para mateiral do drive - https://drive.google.com/drive/u/0/folders/1u1c-t69Re4Tk3VxUcZPwU2wNPDBes9Tn


# 📚 API de Livros e Empréstimos (Django REST Framework)

Esta API permite o gerenciamento de livros e o registro de empréstimos por usuários autenticados via Basic Authentication.

---

## 🔐 Autenticação

A API exige autenticação HTTP Basic.

### Configuração em `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

---

## 🧾 Modelos com Regras de Negócio

### 📘 Livro

```python
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    estoque = models.IntegerField()

    def clean(self):
        if self.estoque < 0:
            raise ValidationError("Estoque não pode ser negativo")
```

### 📄 Empréstimo

```python
from django.contrib.auth.models import User

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_emprestimo = models.DateTimeField(auto_now_add=True)
```

---

## 🎯 Serializers com Validação

### `LivroSerializer`

```python
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

    def validate_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("Estoque não pode ser negativo")
        return value
```

### `EmprestimoSerializer`

```python
class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        read_only_fields = ['usuario', 'data_emprestimo']

    def validate(self, data):
        livro = data['livro']
        quantidade = data['quantidade']

        if livro.estoque < quantidade:
            raise serializers.ValidationError("Estoque insuficiente")
        return data

    def create(self, validated_data):
        livro = validated_data['livro']
        livro.estoque -= validated_data['quantidade']
        livro.save()

        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
```

---

## 🔧 Views com ViewSets

```python
class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    serializer_class = EmprestimoSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfTheObject]

    def get_queryset(self):
        return Emprestimo.objects.filter(usuario=self.request.user)
```

---

## 🔁 Rotas com Routers

```python
router = routers.DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'emprestimos', EmprestimoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

---

## ✅ Funcionalidades

- **CRUD de livros**
- **Registro de empréstimos**
- **Controle de estoque automático**
- **Listagem de empréstimos por usuário**
- **Proteção com autenticação Basic Auth**

---

## 🛠 Requisitos

- Django
- Django REST Framework
