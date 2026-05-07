<img width="328" height="483" alt="uml" src="https://github.com/user-attachments/assets/f6d8d3e8-29f2-490a-9691-abf8bce41928" /><br>

```
@startuml

start

:Selecionar cinema;

:Selecionar filme;

:Informar horário;

:Validar disponibilidade;

if (Horário disponível?) then (Sim)

:Salvar sessão;

:Exibir sucesso;

else (Não)

:Exibir conflito de horário;

endif

stop

@enduml
```
