## Libraries to install if other connections than sqlite


# from sqlalchemy.engine import URL

# username = "postgres"
# password = "pgpasspg2"
# hostname = "jehda-demo-test-db.c3i6cicmqhx7.eu-north-1.rds.amazonaws.com"

# url_object = URL.create(
#     "postgresql+psycopg2",
#     username=username,
#     password=password,
#     host=hostname,
#     database="postgres",
#     port=5432,
# )

# from sqlalchemy import create_engine

# engine = create_engine(url_object, echo=True)

# conn = engine.connect()
# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import Column

# from sqlalchemy import String, Integer


# class Base(DeclarativeBase):
#     pass


# class Customers(Base):
#     __tablename__ = "customers"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     country = Column(String)
#     job = Column(String)
#     age = Column(Integer)


# Base.metadata.create_all(engine)

# customer_01 = Customers(
#     id=4, name="Sauerkraut", country="Germany", job="engineer", age=37
# )
# customer_02 = Customers(
#     id=5, name="Jones", country="United Kingdom", job="journalist", age=52
# )
# customer_03 = Customers(id=6, name="Dupont", country="France", job="dancer", age=25)


# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)

# session = Session()

# session.add(customer_01)
# session.add(customer_02)
# session.add(customer_03)

# session.commit()

# import plotly.express as px

# df = px.data.iris()
# df.head()

# df.to_sql("iris_2", engine)

# df.head()

# from sqlalchemy.sql import text

# statement = text("""
#     SELECT DISTINCT species
#     FROM iris_2
# """)
# result = conn.execute(statement)
# result.fetchall()

# df.head()

# s = text("""
#     SELECT AVG(sepal_length)
#     FROM iris_2
# """)
# result = conn.execute(s)
# result.fetchone()

# statement = text("""
#     SELECT species, avg(sepal_length)
#     FROM iris_2
#     GROUP BY species
# """)
# result = conn.execute(statement)
# result.fetchall()

# statement = text("""
#     SELECT count(*)
#     FROM iris_2
#     WHERE sepal_length < 6 and species = 'virginica'
# """)
# result = conn.execute(statement)
# result.fetchall()

# statement = text("""
#     SELECT species, count(*)
#     FROM iris_2
#     WHERE sepal_length < 6
#     GROUP BY species
# """)
# result = conn.execute(statement)
# result.fetchall()

# # Install the right version of sqlalchemy
# #!pip install sqlalchemy==2.0.0

# # Import sqlalchemy
# from sqlalchemy import create_engine, text

# # Create engine will create a connection between a SQLlite DB and python
# engine = create_engine("sqlite:///:memory:", echo=True)
# # engine = create_engine(f"mysql+pymysql://{DBUSER}:{DBPASS}@{DBHOST}:{PORT}/{DBNAME}", echo=True)
# # engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DBNAME}", echo=True)

# # Let's instanciate a declarative base to be able to use our python class
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# # Let's define our table using a class
# from sqlalchemy import Column, Integer, String


# class User(Base):
#     __tablename__ = "users"

#     # Each parameter corresponds to a column in our DB table
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     nickname = Column(String)

#     def __repr__(self):
#         return "<User(name='{}', fullname='{}', nickname='{}')>".format(
#             self.name, self.fullname, self.nickname
#         )


# # Create a new instance of User will allow us to insert a new record later on
# ed_user = User(id=1, name="ed", fullname="Ed Jones", nickname="edsnickname")

# # Access Full row
# print(ed_user)

# # Access ed_user name
# name = ed_user.name
# print("name: {}".format(name))

# # Access ed_user nickname
# nickname = ed_user.nickname
# print("nickname: {}".format(nickname))


# # Initialize a sessionmaker
# from sqlalchemy.orm import sessionmaker

# Session = sessionmaker(bind=engine)

# # Create a new instance of User will allow us to insert a new record later on
# al_user = User(id=2, name="al", fullname="Al Jones", nickname="alsnickname")

# # Access Full row
# print(al_user)

# # Create a new instance of User will allow us to insert a new record later on
# al_user = User(id=2, name="al", fullname="Al Jones", nickname="alsnickname")

# # Access Full row
# print(al_user)

# # Instanciate Session
# session = Session()

# # Add values to db
# session.add(ed_user)
# session.add(al_user)

# # Commit the results
# session.commit()

# # Query our table users
# user = session.query(User)

# # Output all the results
# user.all()

# from sqlalchemy import text

# # Create a statement
# statement = text("SELECT * FROM users where name=:name")
# statement

# session.query(User).from_statement(statement).params(name="ed").all()

# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

# meta = MetaData()

# # Define table "students"
# students = Table(
#     "students",
#     meta,
#     Column("id", Integer, primary_key=True),
#     Column("name", String),
#     Column("lastname", String),
# )

# # Define table "adresses"
# addresses = Table(
#     "addresses",
#     meta,
#     Column("id", Integer, primary_key=True),
#     Column("email_address", String),
#     Column("student_id", None, ForeignKey("students.id")),
# )

# meta.create_all(engine)

# ins = students.insert().values(id="1", name="Jack", lastname="Johnson")
# ins

# # Connect to the db
# conn = engine.connect()

# # Execute the query
# result = conn.execute(ins)
# conn.commit()

# values = [
#     {"student_id": 1, "email_address": "jack@yahoo.com"},
#     {"student_id": 1, "email_address": "jack@msn.com"},
# ]

# conn.execute(addresses.insert(), values)
# conn.commit()

# from sqlalchemy.sql import text

# # Create a statement
# stmt = text(
#     "SELECT students.id, addresses.id, students.name, addresses.email_address FROM students "
#     "JOIN addresses ON students.id=addresses.student_id "
#     "WHERE students.id = 1"
# )

# result = conn.execute(stmt)

# result.fetchall()

# import pandas as pd

# # Create a statement
# # Within the text() method is a SQL query. Check out our SQL reminder course if you feel a little rusty
# stmt = text(
#     "SELECT students.id, students.name, addresses.email_address FROM students "
#     "JOIN addresses ON students.id=addresses.student_id "
#     "WHERE students.id = 1"
# )

# df = pd.read_sql_query(con=engine.connect(), sql=stmt)

# df.head()
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
from pandas import DataFrame

# Function for Expanding DateTime to separate columns taht can be used for other data


def expand_date(df: DataFrame, datename: str) -> DataFrame:
    """Expand Date/Time column into separate columns for date components."""
    df["date"] = df[datename].dt.date
    df["month"] = df[datename].dt.month
    df["week"] = df[datename].dt.isocalendar().week
    df["MonthDayNum"] = df[datename].dt.day
    df["HourOfDay"] = df[datename].dt.hour
    df["DayOfWeekNum"] = df[datename].dt.dayofweek  # Monday=0, Sunday=6.
    df["DayOfWeek"] = df[datename].dt.day_name()
    return df


def detect_outliers_iqr(data: DataFrame, column: str) -> DataFrame:
    """Detect outliers in a DataFrame column using the IQR method."""
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers
