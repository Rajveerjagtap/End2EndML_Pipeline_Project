# End to End ML Pipeline Project

## Overview
This project implements a comprehensive end-to-end machine learning pipeline that handles the full ML lifecycle from data ingestion to model deployment. It demonstrates best practices in MLOps including data validation, feature engineering, model training with hyperparameter tuning, and containerized deployment with monitoring capabilities.

## Project Structure
```
End2EndML_Pipeline_Project/
├── .github/
│   └── workflows/
│       ├── main.yaml                  # CI/CD pipeline configuration
├── config/
│   ├── config.yaml                    # Main configuration file
│   └── params.yaml                    # Model hyperparameters
├── data/
│   ├── processed/                     # Processed datasets
│   └── raw/                           # Raw input datasets
├── logs/                              # Application logs
├── mlflow/                            # MLflow tracking artifacts
├── models/                            # Saved model artifacts
├── notebooks/                         # Jupyter notebooks for exploration
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py          # Data collection component
│   │   ├── data_transformation.py     # Feature engineering component
│   │   ├── data_validation.py         # Data quality checks
│   │   ├── model_trainer.py           # Model training logic
│   │   └── model_evaluation.py        # Model evaluation logic
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── prediction_pipeline.py     # Inference pipeline
│   │   └── training_pipeline.py       # Training pipeline
│   ├── utils/
│   │   ├── __init__.py
│   │   └── common.py                  # Common utility functions
│   ├── __init__.py
│   ├── exception.py                   # Custom exception handling
│   └── logger.py                      # Logging configuration
├── api/
│   ├── app.py                         # FastAPI application
│   └── Dockerfile                     # Docker configuration for API
├── tests/                             # Unit and integration tests
├── .dvc/                              # DVC configuration files
├── .gitignore                         # Files to be ignored by git
├── dvc.yaml                           # DVC pipeline definition
├── requirements.txt                   # Python dependencies
├── setup.py                           # Package installation setup
└── README.md                          # Project documentation
```

## Key Features

- **Modular Pipeline Architecture**: Components are isolated for better maintainability and testing
- **Automated Data Validation**: Data schema validation to ensure data quality
- **Feature Engineering Pipeline**: Automated transformation with preprocessing steps
- **Hyperparameter Optimization**: Finding optimal model parameters through cross-validation
- **Experiment Tracking**: Using MLflow to track experiments and model versions
- **Data Version Control**: Using DVC to version datasets and model artifacts
- **CI/CD Integration**: Automated testing and deployment workflow
- **Containerized Deployment**: Docker container for consistent deployment
- **API Endpoint**: FastAPI for model serving with documentation
- **Monitoring**: Performance metrics and data drift detection

## Technologies Used

- **Python**: Core programming language
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **Pandas & NumPy**: Data manipulation and processing
- **MLflow**: Experiment tracking and model registry
- **DVC**: Data and model versioning
- **FastAPI**: API development
- **Docker**: Containerization
- **GitHub Actions**: CI/CD pipeline

## Getting Started

### Prerequisites
- Python 3.8+
- Docker (for containerized deployment)
- Git LFS (for large file storage)

### Installation

1. Clone the repository
```bash
git clone https://github.com/Rajveerjagtap/End2EndML_Pipeline_Project.git
cd End2EndML_Pipeline_Project
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up DVC (optional, for data versioning)
```bash
pip install dvc
dvc init
```

### Running the Pipeline

1. Configure the pipeline parameters in `config/config.yaml` and `config/params.yaml`

2. Run the training pipeline
```bash
python src/pipeline/training_pipeline.py
```

3. Start the prediction API
```bash
uvicorn api.app:app --reload
```

4. For Docker deployment
```bash
docker build -t mlpipeline -f api/Dockerfile .
docker run -p 8000:8000 mlpipeline
```

## API Documentation

Once the API is running, you can access the auto-generated documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Model Training and Evaluation

The pipeline includes the following steps:

1. **Data Ingestion**: Collects and organizes raw data
2. **Data Validation**: Validates data quality and schema
3. **Data Transformation**: Performs feature engineering and preprocessing
4. **Model Training**: Trains the ML model with hyperparameter tuning
5. **Model Evaluation**: Evaluates model performance against metrics

## Experiment Tracking

All experiments are tracked using MLflow, providing:
- Parameter tracking
- Metrics logging
- Model artifacts
- Run comparison

Access the MLflow UI by running:
```bash
mlflow ui
```

## CI/CD Pipeline

The project includes GitHub Actions workflows for:
- Running tests
- Building and pushing Docker images
- Automated deployment

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Contact

Rajveer Jagtap - [r5rjagtap@gmail.com](mailto:r5rjagtap@gmail.com)

Project Link: [https://github.com/Rajveerjagtap/End2EndML_Pipeline_Project](https://github.com/Rajveerjagtap/End2EndML_Pipeline_Project)
