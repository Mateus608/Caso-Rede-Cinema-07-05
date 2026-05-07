<img width="437" height="655" alt="plml" src="https://github.com/user-attachments/assets/238ccdf9-b4e0-45fe-b4f9-921e5aafe2a3" /><br>
```
@startuml

left to right direction

actor "Administrador" as Admin
actor "Espectador" as User

rectangle "Sistema Rede de Cinemas" {

  usecase "Cadastrar Filme" as UC1
  usecase "Cadastrar Cinema" as UC2
  usecase "Cadastrar Sessão" as UC3
  usecase "Registrar Público" as UC4
  usecase "Consultar Filmes em Cartaz" as UC5
  usecase "Consultar Público por Filme" as UC6
  usecase "Consultar Público por Cinema" as UC7
  usecase "Consultar Informações do Filme" as UC8

}

Admin --> UC1
Admin --> UC2
Admin --> UC3
Admin --> UC4
Admin --> UC6
Admin --> UC7

User --> UC5
User --> UC8

@enduml
```
