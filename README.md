# 📓 2. DIÁRIO DIGITAL COM TAGS E EMOÇÕES
Tipo uma versão minimalista do Daylio, voltado pra registro emocional.

**Funcionalidades**:

- Registro de entradas diárias (sentimento(bem, neutro, mal), emoção, texto)

- Filtros e buscas
  - texto por emoção(bem, neutro, mal)
  - sentimento por emoção

- CRUD de entradas

- Login/JWT

- Stack:

- FastAPI + SQLAlchemy

- postgreSQL


## **CHECK LIST**:

- [ x ] gerar e verificar o jwt
- [ x ] gerar hash da senha e verificar
- [  ] endpoint de login
- [  ] endpoint de signup
- [  ] endpoints de read GET
- [  ] endpoints de create POST
- [  ] endpoints de update PUT/PATCH
- [  ] endpooints para delete DELETE
- [  ] configurar as origens com o CORS
- [  ] implementar o banco
  - [  ] criar as tabelas
  - [  ] criar o model que vai manipular o banco
    - [  ] consultas select
    - [  ] consultas insert
    - [  ] consultas update
    - [  ] consultas delete




 [life-note-api](https://github.com/HiagoHenrique2007/life-note-api)

### ✅ Pontos Positivos

1. **Uso do FastAPI com Tipagem**: Você está utilizando o FastAPI com tipagem explícita, o que melhora a legibilidade e a manutenção do código.

2. **Separação de Schemas**: A definição de modelos Pydantic para validação de dados está clara e organizada, o que é essencial para a robustez da API.

3. **Endpoints Bem Definidos**: Os endpoints estão estruturados de forma clara, facilitando a compreensão das rotas disponíveis.

---

### 🔧 Sugestões de Melhoria

1. **Estrutura de Projeto Modular**: Para facilitar a escalabilidade e manutenção, considere reorganizar seu projeto em uma estrutura modular Uma abordagem comum é separar o código em diretórios como `routers`, `models`, `schemas`, `services` e `core` Isso ajuda a manter o código organizado à medida que o projeto cresce.

2. **Integração com Banco de Dados**: Como mencionado, a integração com o banco de dados ainda está pendente Recomenda-se o uso do SQLAlchemy para ORM, juntamente com o Alembic para migrações Isso proporcionará uma base robusta para operações de CRUD e facilitará a evolução do esquema do banco de dados

3. **Camada de Serviços**: Introduza uma camada de serviços para encapsular a lógica de negócios. Isso separa as responsabilidades entre as rotas (que lidam com requisições e respostas) e a lógica de aplicação, promovendo um código mais limpo e testável.

4. **Tratamento de Exceções Centralizado**: Implemente um manipulador global de exceções para capturar e tratar erros de forma consistente em toda a aplicação Isso melhora a experiência do usuário e facilita a depuração

5. **Validação de Dados**: Embora você esteja validando dados com Pydantic, considere adicionar validações adicionais, como verificar se pelo menos um campo foi fornecido em atualizações parciais Isso pode ser feito com validadores personalizados

6. **Documentação da API**: Aproveite os recursos do FastAPI para documentar sua API automaticamente Certifique-se de que todas as rotas, modelos e parâmetros estejam bem descritos para facilitar o uso por outros desenvolvedores

7. **Testes Automatizados**: Mesmo em um MVP, é benéfico começar a implementar testes automatizados Utilize ferramentas como `pytest` para criar testes unitários e de integração, garantindo que as funcionalidades principais estejam funcionando conforme o esperado

---

### 📁 Estrutura de Projeto Sugerida
Uma estrutura de projeto recomendada para aplicações FastAPI :

```plaintext
life-note-api/
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── record.py
│   ├── schemas/
│   │   └── record.py
│   ├── services/
│   │   └── record_service.py
│   ├── routers/
│   │   └── record_router.py
│   └── db/
│       ├── base.py
│       └── session.py
├── tests/
│   └── test_record.py
├── requirements.txt
└── alembic/
    └── ...
``

Essa estrutura promove uma separação clara de responsabilidades e facilita a escalabilidade do projeto.



