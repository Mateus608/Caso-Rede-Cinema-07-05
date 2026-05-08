# Rede de Cinemas
### Estrutura de Pastas
```
rede-cinemas/
│
├── docs/
│   ├── requisitos.md
│   ├── regras-negocio.md
│   ├── casos-de-uso.puml
│   ├── diagrama-classes.puml
│   ├── atividade-cadastrar-sessao.puml
│   ├── atividade-registrar-publico.puml
│   ├── sequencia-cadastrar-sessao.puml
│   └── sequencia-registrar-publico.puml
│
├── src/
│   ├── controller/
│   │   ├── FilmeController.java
│   │   └── SessaoController.java
│   │
│   ├── service/
│   │   ├── FilmeService.java
│   │   └── SessaoService.java
│   │
│   ├── repository/
│   │   ├── FilmeRepository.java
│   │   ├── SessaoRepository.java
│   │   └── ConnectionFactory.java
│   │
│   ├── model/
│   │   ├── Cinema.java
│   │   ├── Filme.java
│   │   ├── Sessao.java
│   │   ├── Diretor.java
│   │   ├── Genero.java
│   │   └── Elenco.java
│   │
│   ├── view/
│   │   └── Main.java
│   │
│   └── database/
│       └── cinema.db
│
└── README.md
```

## Fluxo da Aplicação
```
main.py
 ↓
View
 ↓
Controller
 ↓
Service
 ↓
Repository
 ↓
SQLite
```

## Como executar

Para iniciar a aplicação, execute no seu terminal o comando `python src/main.py`

<img width="1536" height="1024" alt="view" src="https://github.com/user-attachments/assets/5c3fde4d-e921-4ec9-9c94-c7237e031eb3" />
