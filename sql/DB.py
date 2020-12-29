from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float
from model.Constants import ApiConstants
import requests
from sqlalchemy.orm import sessionmaker
import json


class DBCreator():

    def initialize(self):

        engine = create_engine('sqlite:///memory.db', echo=True)
        Base = declarative_base(bind=engine)

        class Food(Base):
            __tablename__ = 'food'

            id = Column(String, primary_key=True)
            name = Column(String, primary_key=True)
            kcal = Column(Float)
            carbs = Column(Float)
            fat = Column(Float)
            protein = Column(Float)

        Food.__table__.create(bind=engine, checkfirst=True)

        food_list = []

        def get_api_response(original_key, original_food_id):

            response = requests.get(ApiConstants.URL + str(original_food_id) + ApiConstants.KEY)
            if response.status_code == 200:
                row = dict()
                row["id"] = original_key
                row["name"] = response.json()['description']

                for item in response.json()['foodNutrients']:
                    if item['nutrient']['name'] == 'Energy':
                        row["kcal"] = float(item['amount'])
                    elif item['nutrient']['name'] == 'Carbohydrate, by difference':
                        row["carbs"] = float(item['amount'])
                    elif item['nutrient']['name'] == 'Protein':
                        row["protein"] = float(item['amount'])
                    elif item['nutrient']['name'] == 'Fatty acids, total saturated':
                        row["fat"] = float(item['amount'])

                food_list.append(row)

        with open("food_ids.json") as json_file:
            data = json.load(json_file)
            for key, food_id in data.items():
                get_api_response(key, food_id)

        Session = sessionmaker(bind=engine)
        session = Session()

        for food in food_list:
            row = Food(**food)
            session.add(row)

        session.commit()

