# Anotações

- Para iniciar o alembic no projeto:
    ```
    $ alembic init migrations
    ```

- Para apontar para o banco de dados correto alteramos `sqlalchemy.url` em "alembic.ini":
    ```
    sqlalchemy.url = sqlite:///models.db
    ```

- Para importar as tabelas corretas fazemos alterações em "migrations/env.py":
    ```
    -- from myapp import mymodel
    -- target_metadata = mymode.Base.metadata
    ```
    ```
    ++ from models import Base
    ++ target_metadata = Base.metadata
    ```

- Como em "models.py", criamos os modelos de tabelas.py. Os modelos devem ser classes que herdam de `declarative_base`.

- Para criar uma migração dentro de "migrations/versions":
    ```
    $ alembic revision --autogenerate -m "Create user model"
    ```

- Para aplicar a última migração criada ao banco de dados:
    ```
    $ alembic upgrade heads
    ```

## Erros

- "No support for ALTER of constraints in SQLite dialect"
    - Solução: editar "env.py" adicionando `render_as_batch=True` em `context.configure`.
    - Fonte: https://stackoverflow.com/questions/30378233/sqlite-lack-of-alter-support-alembic-migration-failing-because-of-this-solutio