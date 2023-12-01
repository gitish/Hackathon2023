# Base Python image
FROM python:3.7

# Set working directory
WORKDIR /app  

# Copy requirements
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Copy app code
COPY . .

# Expose port  
EXPOSE 5000

# Run app.py on start up  
CMD ["python", "app.py"]