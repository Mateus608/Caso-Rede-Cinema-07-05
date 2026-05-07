<img width="778" height="444" alt="diagram3" src="https://github.com/user-attachments/assets/03106892-1634-4f67-bbb2-8d09db4f60a1" /><br>

```
@startuml

actor Administrador

boundary View
control SessaoController
control SessaoService
entity SessaoRepository
database SQLite

Administrador -> View : Informar público
View -> SessaoController : registrarPublico()

SessaoController -> SessaoService : validarCapacidade()

SessaoService -> SessaoRepository : atualizarPublico()

SessaoRepository -> SQLite : UPDATE sessão

SQLite --> SessaoRepository : confirmação

SessaoRepository --> SessaoService : atualizado

SessaoService --> SessaoController : sucesso

SessaoController --> View : exibir mensagem

@enduml
```
