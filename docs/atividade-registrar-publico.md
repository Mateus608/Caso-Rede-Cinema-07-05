<img width="307" height="375" alt="uml2" src="https://github.com/user-attachments/assets/16bb7641-06f6-44e6-bab1-c25f50574577" /><br>

```
@startuml

start

:Selecionar sessão;

:Informar quantidade de público;

if (Capacidade excedida?) then (Sim)

:Exibir erro;

else (Não)

:Salvar público;

:Atualizar relatório;

endif

stop

@enduml
```
