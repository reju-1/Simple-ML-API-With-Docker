# Iris Prediction API

This FastAPI project predicts the species of iris flowers using an SVM model based on sepal and petal measurements.

## The project is divided into 2 section
- model-creation 
- web-server
first we need create the model. then save the .pkl (pickle file)
into web-server directory 

## Requirements
- Python 3.10+
- `requirements.txt` dependencies

## Running Without Docker

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI app:
    ```bash
    uvicorn main:app --reload
    ```

4. Access the API at `http://127.0.0.1:8000/`.

## Running with Docker

1. Build the Docker image:
    ```bash
    docker build -t iris-prediction-api .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 8000:8000 iris-prediction-api
    ```

## API Endpoints
- `GET /` - Health check.
- `POST /predict/` - Predict iris species.

## License
MIT License
