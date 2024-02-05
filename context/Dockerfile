# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the script and any required files to the container
COPY azure_mgmt_containerregistry-10.3.0-py3-none-any.whl create_acr.py /app/

# Install Azure SDK and other dependencies
RUN pip install azure_mgmt_containerregistry-10.3.0-py3-none-any.whl azure-identity

# Run the Python script when the container starts
CMD ["python", "create_acr.py"]