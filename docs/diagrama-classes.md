<img width="467" height="339" alt="diagram" src="https://github.com/user-attachments/assets/881eec0a-1cf6-4741-9945-d37cb6f55ca0" /><br>

```
@startuml

class Cinema {
  id
  nome
  endereco
  capacidade
  cidade
  estado
}

class Filme {
  id
  titulo
  duracao
  classificacao
}

class Sessao {
  id
  horarioInicio
  horarioFim
  publico
}

class Diretor {
  id
  nome
}

class Genero {
  id
  nome
}

class Elenco {
  id
  nome
}

Cinema "1" -- "*" Sessao
Filme "1" -- "*" Sessao
Filme "*" -- "*" Genero
Filme "*" -- "*" Elenco
Filme "*" -- "1" Diretor

@enduml
```
