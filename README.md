# Chicken Disease Detection

This project leverages deep learning models to accurately detect various chicken diseases from image data. The primary goal is to assist in early disease identification, which can significantly reduce economic losses in poultry farming.

## Features

*   **Image Classification**: Classify chicken images into healthy or diseased categories.
*   **Data Handling Utilities**: `src/chicken_classifier/utils/common.py` provides robust utility functions for:
    *   Reading and writing YAML and JSON configuration files.
    *   Creating directories.
    *   Saving and loading binary data (e.g., trained models).
    *   Decoding base64 encoded images.
    *   Calculating file sizes.
*   **Modular Project Structure**: Organized codebase for scalability and maintainability.

## Installation

To set up the project locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/Chicken-Disease-Detection.git
    cd Chicken-Disease-Detection
    ```

2.  **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Detailed instructions on how to train the model, make predictions, or run the application will be provided here.

## Project Structure

```
.
├── src/
│   └── chicken_classifier/
│       ├── utils/
│       │   └── common.py         # Utility functions
│       └── ...                   # Other modules (components, pipeline, etc.)
├── config/                       # Configuration files (e.g., model params, data paths)
├── data/                         # Raw and processed datasets
├── notebooks/                    # Jupyter notebooks for experimentation
├── saved_models/                 # Trained model artifacts
├── requirements.txt              # Project dependencies
├── README.md
└── ...
```

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License