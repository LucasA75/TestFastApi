from typing import Optional

from sqlmodel import Field, SQLModel, create_engine,Session


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

def crearHeroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    hero_4 = Hero(name="Rusty-Man", secret_name=2, age=48)

with Session(engine) as session:
    session.add(hero_4)
    session.commit()

def main():
    crearHeroes()

if __name__ == "__main__":
    main()