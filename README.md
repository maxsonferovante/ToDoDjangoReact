
# To-Do Django Rest Api

Api Rest que servirá o To-Do React

## Referência

 - [Django](https://docs.djangoproject.com/en/4.2/)
 

## Funcionalidades

- Adição de Tarefas
- Exclusão das Tarefas cadastradas
- Edição das Tarefas
- Consulta por ID e ALL


## Documentação da API

#### Retorna todos os tarefas

```http
  GET /api/todos
  Exemplo do retorno
    [
      {
          "id": 1,
          "title": "title - 1",
          "description": " description - 1",
          "completed": true
      },
      {
          "id": 2,
          "title": "title - 2",
          "description": "description ",
          "completed": false
      },
      {
          "id": 3,
          "title": "title - 3",
          "description": "description ",
          "completed": true
      },
    ]
```
#### Retorna uma tarefa

```http
  GET /api/todos/${id}
  Exemplo do retorno
  {
      "id": 1,
      "title": "Passer com a Toinha",
      "description": "Fazer isso antes das 17h",
      "completed": true
  }
```


## Autores

- [@maxsonferovante](https://www.github.com/maxsonferovante)


## Usado por

Esse projeto é usado pelas seguintes empresas:

- To Do React - https://todoreact.herokuapp.com/



