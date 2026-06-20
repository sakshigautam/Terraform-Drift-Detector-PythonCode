FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y wget unzip

RUN wget https://releases.hashicorp.com/terraform/1.11.0/terraform_1.11.0_linux_amd64.zip

RUN unzip terraform_1.11.0_linux_amd64.zip

RUN mv terraform /usr/local/bin/

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app/main.py"]
