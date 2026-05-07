<img width="800" height="444" alt="diagram2" src="https://github.com/user-attachments/assets/20548a7b-7099-47e0-9031-c5218d4f184c" /><br>

```
@startuml

actor Administrador

boundary View
control SessaoController
control SessaoService
entity SessaoRepository
database SQLite

Administrador -> View : Informar dados da sessão
View -> SessaoController : cadastrarSessao()

SessaoController -> SessaoService : validarSessao()

SessaoService -> SessaoRepository : salvar()

SessaoRepository -> SQLite : INSERT sessão

SQLite --> SessaoRepository : confirmação

SessaoRepository --> SessaoService : sessão salva

SessaoService --> SessaoController : sucesso

SessaoController --> View : exibir mensagem

@enduml
```
