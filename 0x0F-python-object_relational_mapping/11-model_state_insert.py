#!/usr/bin/python3
""" Adds Louisiana to list of state names
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = State(name='Louisiana')
    session.add(new_state)
    new_inst = session.query(State).filter_by(name='Louisiana').first()
    print(new_inst.id)
    session.commit()
