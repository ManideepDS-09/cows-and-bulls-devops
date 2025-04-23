# lightweight official image with Python 3.10 and minimal packages
FROM python:3.10-slim

# From here on, run all commands inside a specific folder in the container.
WORKDIR /app

# Copy everything from my project folder into the /app folder inside the container.
COPY . .

# Install all Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to start/run the app
CMD ["python", "main.py"]
