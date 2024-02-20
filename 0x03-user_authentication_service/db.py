#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add user to database
        Args:
            email (str): user email
            hashed_password (str): hashed password
        Return:
            User: return user object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """find user by kwargs
        Returns:
            User: found user
        """

        try:
            users = self._session.query(User).filter_by(**kwargs).all()
        except InvalidRequestError as e:
            raise e

        if len(users) == 0:
            raise NoResultFound

        return users[0]

    def update_user(self, user_id: str, **kwargs) -> None:
        """update user by id
        Args:
            user_id (str): user id
        """

        try:
            user = self.find_user_by(id=user_id)

            try:
                for key, value in kwargs.items():
                    setattr(user, key, value)
            except ValueError as e:
                raise e

            self.__session.add(user)
            self._session.commit()

        except (InvalidRequestError, NoResultFound) as e:
            pass
