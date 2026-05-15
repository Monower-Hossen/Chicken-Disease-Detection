# Chicken Disease Detection using Deep Learning

This project implements an advanced deep learning solution for the accurate and early detection of various chicken diseases from image data. By leveraging state-of-the-art Convolutional Neural Networks (CNNs), the system aims to provide a crucial tool for poultry farmers to identify health issues swiftly, thereby minimizing disease spread, reducing economic losses, and improving overall flock health and productivity.

Early disease identification is paramount in poultry farming, where outbreaks can lead to devastating consequences. This system offers a robust, AI-powered approach to automate and enhance the diagnostic process.

## Features

*   **Advanced Image Classification**: Utilizes deep learning models (specifically CNNs) to classify chicken images into "Healthy" or various "Diseased" categories with high accuracy. This enables rapid and non-invasive diagnosis.
*   **Robust Data Handling & Configuration Management**: The `src/chicken_classifier/utils/common.py` module provides a suite of essential utility functions:
    *   **Configuration Management**: Seamlessly reads and writes YAML and JSON configuration files, ensuring standardized parameter management for experiments and deployments.
    *   **Directory Management**: Automated creation of necessary directory structures for organized data, logs, and model artifacts.
    *   **Model Persistence**: Efficient saving and loading of binary data (e.g., trained machine learning models using `joblib`) for reusability and deployment.
    *   **Image Preprocessing**: Utilities for decoding base64 encoded images, facilitating web-based image submissions.
    *   **System Utilities**: Functions for calculating file sizes, useful for monitoring and resource management.
*   **Modular and Scalable Architecture**: The project is structured with a clear separation of concerns, following MLOps best practices. This modularity enhances maintainability, facilitates collaboration, and allows for easy integration of new features or model architectures.
*   **Web-based Prediction Interface**: Includes a lightweight Flask web application (`app.py`) that provides a user-friendly interface for uploading images and receiving real-time disease predictions.
*   **MLOps Readiness**: Incorporates `dvc.yaml` for Data Version Control and `params.yaml` for managing hyperparameters, laying the groundwork for reproducible machine learning pipelines and easier deployment.

## Technologies Used

*   **Python**: Primary programming language.
*   **Flask**: Web framework for the prediction API.
*   **TensorFlow/Keras**: (Implied by deep learning) For building and training CNN models.
*   **scikit-learn/joblib**: For model serialization.
*   **PyYAML, json, box**: For configuration management.
*   **DVC (Data Version Control)**: For managing data and model versions (planned/integrated).
*   **Docker**: For containerization and deployment (planned/integrated).

## Installation

To set up and run this project locally, please follow these steps:

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Steps

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Monower-Hossen/Chicken-Disease-Detection
    cd Chicken-Disease-Detection
    ```
    *(Replace `your-username` with the actual GitHub username or organization.)*

2.  **Create a virtual environment (recommended)**:
    It's highly recommended to use a virtual environment to manage project dependencies and avoid conflicts with other Python projects.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    # If you plan to use DVC, install it separately:
    # pip install dvc
    ```

## Usage

This project supports both model training and real-time prediction via a web interface.

### 1. Model Training and Experimentation

The `research/` directory contains Jupyter notebooks for exploratory data analysis, model prototyping, and training experiments. For a full end-to-end ML pipeline execution (data ingestion, preparation, training, evaluation), you would typically run the `main.py` script.

```bash
# Example: Running the main ML pipeline (ensure configurations in config/ and params/ are set)
python main.py
```

### 2. Real-time Prediction via Web Application

The `app.py` file hosts a Flask web application that allows users to upload images and get instant disease predictions.

```bash
python app.py
```
Once the server is running, open your web browser and navigate to `http://0.0.0.0:8080` (or `http://127.0.0.1:8080` on most local setups). You can then upload a chicken image to receive a prediction.

## Project Structure

```
.
├── src/
│   └── chicken_classifier/
│       ├── __init__.py           # Makes `chicken_classifier` a Python package
│       ├── components/           # Modular building blocks of the ML pipeline (e.g., data ingestion, model training)
│       ├── utils/                # General utility functions (e.g., common.py for I/O, logging)
│       │   └── common.py         # Core utility functions for file operations, config, etc.
│       ├── config/               # Configuration management for the ML pipeline
│       │   └── configuration.py  # Manages configuration settings
│       ├── pipeline/             # Defines the end-to-end ML pipeline stages
│       │   └── prediction.py     # Contains the prediction pipeline logic for inference
│       ├── entity/               # Data classes/entities for type-safe data handling
│       └── constants/            # Stores project-wide constants
├── config/                       # Project-level configuration files
│   └── config.yaml               # Main configuration file for the project
├── data/                         # Directory for raw and processed datasets
├── notebooks/                    # Jupyter notebooks for research, experimentation, and prototyping
├── saved_models/                 # Stores trained model artifacts and checkpoints
├── requirements.txt              # Lists all Python dependencies required for the project
├── dvc.yaml                      # Data Version Control configuration for data and model versioning
├── params.yaml                   # Stores hyperparameters and other pipeline parameters
├── setup.py                      # Setup script for packaging the project
├── main.py                       # Entry point for running the complete ML pipeline
├── app.py                        # Flask web application for prediction inference
├── Dockerfile                    # Dockerfile for containerizing the application
├── .gitignore                    # Specifies intentionally untracked files to ignore
├── templates/                    # HTML templates for the Flask web UI (e.g., index.html)
├── README.md                     # Project overview and documentation
└── .github/workflows/            # GitHub Actions CI/CD workflows (e.g., for automated testing, deployment)
```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License