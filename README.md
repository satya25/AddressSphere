# AddressSphere

AddressSphere is an address management system that provides a REST API for CRUD operations. It allows users to create, read, update, and delete address records efficiently.

## Features

- REST API for address management
- Unit tests to ensure code quality
- Docker support for containerization
- Kubernetes configuration for deployment
- Jenkins pipeline for CI/CD

## Getting Started

### Prerequisites

- Python 3.9+
- Docker
- Kubernetes (Minikube)
- Jenkins

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/AddressSphere.git
    cd AddressSphere
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Unix or MacOS
    .\venv\Scripts\activate  # On Windows
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the application locally:
```bash
python run.py
