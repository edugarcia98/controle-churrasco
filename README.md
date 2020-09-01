# Churrasco Hammer

## Iniciando o sistema

### Configurando o banco de dados

O banco de dados utilizado para essa aplicação é o PostgreSQL. Para configurá-lo, deve-se primeiramente criar um novo banco de dados no PostgreSQL e definir um usuário owner para o mesmo.
Após criado o banco de dados, deve-se editar o arquivo .env, que está no diretório churrasco_hammer, da seguinte maneira:

```
NAME=[DB_NAME]
USER=[DB_USER]
PASSWORD=[DB_PASSWORD]
HOST=[HOST]
PORT=[PORT]
```

### Subindo a aplicação

Para se executar a aplicação, devem ser executados os seguintes comandos dentro do diretório churrasco_hammer:

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Esses comandos irão instalar as bibliotecas, criar as tabelas banco de dados e executar a API que, por padrão será executada na seguinte URL:

```
http://127.0.0.1:8000/
```

OBS.: Iremos considerar essa URL padrão, mas, para alterá-la, pode-se definir outro IP, com o seguinte comando:

```
python manage.py runserver [IP]:[PORTA]
```

## Pessoas

As pessoas podem ser funcionários ou convidados. Deve-se considerar que cada funcionário pode levar apenas um convidado.

### Participar do churrasco

Portanto, para efetivar a participação de um convidado no churrasco, deve-se realizar uma requisição, com o método POST, na URL:

```
http://127.0.0.1:8000/api/participar-churrasco/
```

Com o seguinte conteúdo como body:

```
{
    "nome": "Funcionário",
    "bebe": true,
    "convidado": {
        "nome": "Convidado",
        "bebe": false
    }
}
```

Caso o funcionário não deseje levar convidado, pode-se definir o convidado como null, como no seguinte exemplo:

```
{
    "nome": "Funcionário 2",
    "bebe": true,
    "convidado": null
}
```

É esperado então que o valor que um funcionário precisa pagar seja definido a partir dos seguintes parâmetros: se bebe, se está levando convidado e se esse convidado bebe, caso exista.

Após esse cálculo, é esperado que o funcionário e o convidado, se existir, sejam criados na base de dados.

Um exemplo do conteúdo de resposta desta requisição é o seguinte:

```
{
  "nome": "Funcionário",
  "bebe": true,
  "convidado": {
    "nome": "Convidado",
    "bebe": false
  }
}
```


### Cancelar participação

Para que um funcionário ou um convidado cancele sua participação no churrasco, deve-se realizar uma requisição, com o método DELETE, na URL:

```
http://127.0.0.1:8000/api/cancelar-participacao/<id_pessoa>/
```

É esperado então que, caso a pessoa seja um funcionário, sua participação e a do seu convidado, se este existir, sejam cancelados, e, caso a pessoa seja um convidado, apenas sua participação seja cancelada, recalculando o valor a pagar para o funcionário.

Para cancelar a participação, não é esperado nenhum conteúdo como resposta.

### Exibir total arrecadado

Para se exibir o total arrecadado para o churrasco, deve-se realizar uma requisição, com o método GET, na URL:

```
http://127.0.0.1:8000/api/total-arrecadado/
```

É esperado que seja exibido o total arrecadado, tendo o seguinte conteúdo como um exemplo de resposta:

```
{
  "total_arrecadado": 110.0
}
```

### Listar Funcionários

Para se listar os funcionários que participarão do churrasco, deve-se realizar uma requisição, com o método GET, na seguinte URL:

```
http://127.0.0.1:8000/api/funcionarios/
```

É esperado então obter como resposta as informações de todos os funcionários que participarão do churrasco, como no seguinte exemplo:

```
[
  {
    "id": 2,
    "nome": "Funcionário 1",
    "bebe_desc": "Sim",
    "valor_pagar": 30.0
  },
  {
  "id": 8,
  "nome": "Funcionário 2",
  "bebe_desc": "Não",
  "valor_pagar": 20.0
  }
]
```

### Listar convidados

Para se listar os convidados dos funcionários que participarão do churrasco, deve-se realizar uma requisição, com o método GET, na seguinte URL:

```
http://127.0.0.1:8000/api/convidados/
```

É esperado então obter como resposta as informações de todos os convidados dos funcionários que participarão do churrasco, como no seguinte exemplo:

```
[
  {
    "id": 27,
    "nome": "Convidado",
    "bebe_desc": "Não"
  }
]
```

## Compras

As compras podem ser tanto comidas quanto bebidas, e deve-se realizar o controle das mesmas.

### Cadastrar compra

Para se cadastrar uma compra, deve ser realizada uma requisição, com método POST, na seguinte URL:

```
http://127.0.0.1:8000/api/compras/
```

Passando, como corpo da requisição, a seguinte estrutura:

```
{
    "desc": "Compra 1",
    "tipo": 1,
    "preco_unitario": 8,
    "qtd": 2
}
```

OBS.: Tipo 1 é comida e Tipo 2 é bebida.

Espera-se que a compra seja salva no banco de dados e o valor total da mesma seja calculado. É esperado também obter o seguinte conteúdo como resposta:

```
{
  "desc": "Compra 1",
  "tipo": 1,
  "preco_unitario": 8.0,
  "qtd": 2
}
```

### Exibir compras

Para se exibir as compras, deve ser realizada uma requisição, com método GET, na seguinte URL:

```
http://127.0.0.1:8000/api/compras/
```

Esperando-se obter o seguinte conteúdo como resposta:

```
[
  {
    "id": 9,
    "desc": "Compra 1",
    "tipo": 1,
    "preco_unitario": 8.0,
    "qtd": 2,
    "preco_total": 16.0
  }
]
```

### Atualizar compra

Para se realizar o update de alguma compra, deve-se realizar uma requisição, com o método PUT, na seguinte URL:

```
http://127.0.0.1:8000/api/compras/<id_compra>/
``` 

Passando, como corpo da requisição, a seguinte estrutura:

```
{
    "desc": "Compra 1",
    "tipo": 1,
    "preco_unitario": 8,
    "qtd": 4
}
```

Espera-se que a compra seja atualizada no banco de dados e o valor total da mesma seja recalculado. É esperado também obter o seguinte conteúdo como resposta:

```
{
  "id": 19,
  "desc": "Compra 1",
  "tipo": 1,
  "preco_unitario": 8.0,
  "qtd": 4,
  "preco_total": 32.0
}
```

### Excluir compra

Para se excluir alguma compra, deve-se realizar uma requisição, com o método DELETE, na seguinte URL:

```
http://127.0.0.1:8000/api/compras/<id_compra>/
``` 

É esperado que a compra seja excluída do banco de dados e não é esperado nenhum conteúdo como resposta.

### Exibir total gasto

Para se exibir o total gasto em compras, deve-se realizar uma requisição, com o método GET, na URL:

```
http://127.0.0.1:8000/api/total-compras/
```

É esperado que seja exibido o total gasto com todas as compras, tendo o seguinte conteúdo como um exemplo de resposta:

```
{
  "total_gasto": 365.0
}
```

### Exibir total gasto em comida

Para se exibir o total gasto em compras relacionadas a comidas, deve-se realizar uma requisição, com o método GET, na URL:

```
http://127.0.0.1:8000/api/total-compras/comida/
```

É esperado que seja exibido o total gasto com compras em comida, tendo o seguinte conteúdo como um exemplo de resposta:

```
{
  "total_gasto_comida": 293.0
}
```

### Exibir total gasto em bebida

Para se exibir o total gasto em compras relacionadas a bebidas, deve-se realizar uma requisição, com o método GET, na URL:

```
http://127.0.0.1:8000/api/total-compras/bebida/
```

É esperado que seja exibido o total gasto com compras em comida, tendo o seguinte conteúdo como um exemplo de resposta:

```
{
  "total_gasto_bebida": 72.0
}
```