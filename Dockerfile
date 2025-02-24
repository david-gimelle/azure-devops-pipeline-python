# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Install pip and system dependencies
RUN apk add --no-cache \
    curl \
    gcc \
    g++ \
    musl-dev \
    python3-dev \
    rust \
    cargo \
    linux-headers \
    make \
    && pip install --upgrade pip

# Set environment variables
ENV POETRY_VERSION=1.1.11
ENV PYTHONUNBUFFERED=1
ENV CARGO_NET_GIT_FETCH_WITH_CLI=true

# Install Poetry using pip
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install the dependencies (remove --no-dev to include uvicorn)
RUN poetry install --no-root

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5001

# Define the command to run the application using uvicorn
CMD ["poetry", "run", "uvicorn", "app.routes:app", "--host", "0.0.0.0", "--port", "5001"]