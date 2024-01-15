FROM python:3.9-slim

#Set the working directory
WORKDIR /researchproject-image

#python scripts
COPY ./ /researchproject-image/

# Run main.py
CMD ["python", "main.py"]
#Terminal Commands
#docker image build -t research-app:1.0 ./
# docker tag research-app1.0 tahab1/research-app:1.0
