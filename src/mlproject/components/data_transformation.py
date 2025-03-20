import sys
from dataclasses import dataclass
import numpy as np 
import pandas as pd

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import os

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation.
        '''
        try:
            numerical_clonms = ["writing_score", "reading_score"]
            catagorical_column = [
                "gender",
                "race_ethinicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course" 
            ]
            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ])
            cat_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehotencoder", OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ])
            logging.info(f"Numerical columns: {numerical_clonms}")
            logging.info(f"Categorical columns: {catagorical_column}")
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_clonms),
                    ("cat_pipeline", cat_pipeline, catagorical_column)
                ]
            )
            return preprocessor


        except Exception as e:
            raise CustomException(e, sys)
            logging.info('Data transformation completed successfully.')

