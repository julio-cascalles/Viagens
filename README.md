API _Viagens_ (estudo)
---
**por Júlio Cascalles**

---

O objetivo dessa API é simular uma agência de viagens, onde será possível:
* Pesquisar hotéis disponíveis numa determinada cidade;
* Pesquisar os passeios por cidade;
* Pesquisar os passeios por cidade e numa data específica;
* Fazer reserva num hotel e comprar pacote de passeios;
* Consumir o pacote de passeios, fazendo check-in e checkout automáticos quando iniciar e terminar o pacotec;
* Cadastrar novos hotéis;
* Cadastrar novos passeios;

## Regras
> Hotel
* Só podem ser feita uma reserva se houver vaga no hotel;
* Check-in: Só pode ser feito se houver reserva para o hóspede;
* Valor da diária: Calculado pela classificação em `estrelas` do hotel;
* Tamanho do hotel: Determina o número de quartos;

> Passeio
* Só pode ser feito num determinado dia da semana
* Os dias da semana devem ser um desses:
    - seg, ter, qua, qui, sex, sab ou dom
* Os passeios de um hóspede são ordenados por dia da semana
* O formato da data (quando houver) deve ser _dd-mm--yyyy_

> Pacote
* Ao fazer a reserva, a lista de passeios deve conter os nomes separados **por vírgula**;
* Só serão considerados os passeios encontrados;
* Se nenhum passeio for encontrado, o pacote não poderá ser contratado;
* Se o hotel não for encontrado ou se não houver vagas, a reserva não poderá ser feita;
* Será retornado o número do quarto reservado para o hóspede
    - Os números de quarto vão de zero até o tamanho do hotel menos 1.


## Banco de dados, ORM e frameworks...
* Neste projeto o banco de dados é MongoDB, acessado localmente;
* Nenhum ORM de terceiros foi utilizado
    - Em vez disso, criei minha classe de acesso no melhor estilo "clean code"
* As dependências utilizadas são:
    - pyMongo
    - pydantic
    - FastAPI
    - uvicorn

## Testes unitários
`Ainda não disponíveis no projeto...`
