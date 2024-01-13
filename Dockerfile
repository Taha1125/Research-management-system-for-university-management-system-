FROM python:3.9-slim

#Set the working directory
WORKDIR /app

#python scripts
COPY main.py .
COPY researcher.py .
COPY researcherproject.py .
COPY researchmanagementsystem.py .

# Run main.py
CMD ["python", "main.py"]
#Terminal Commands
#docker build -t Research-app
# docker run Research-app 