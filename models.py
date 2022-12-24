from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, create_engine

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return (
            f'UserModel(id={self.id}, first_name={self.first_name}, '
            f'last_name={self.last_name}, birth={self.birth}, created={self.created})'
        )

# Inserindo dados no banco
users = [
    UserModel(first_name='Bob', last_name='Preston', birth=datetime(1980, 5, 2)),
    UserModel(first_name='Susan', last_name='Sage', birth=datetime(1979, 6, 12))
]

## Criando uma sessão para aplicar as inserções
session_maker = sessionmaker(bind=create_engine('sqlite:///models.db'))

def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

# create_users()

# Obtendo dados do banco
with session_maker() as session:
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user)
        print(user.full_name)