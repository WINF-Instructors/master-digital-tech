# Variante 1: nur api
FROM python:latest

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src/ src/
ENTRYPOINT [ "python", "/app/src/start_server.py" ]

# Variante 2: mit ssh
#FROM python:latest

#RUN apt update && apt install  openssh-server sudo -y

#RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test 

# RUN echo 'test:test' | chpasswd

# RUN service ssh start

# EXPOSE 22

# WORKDIR /app

# COPY requirements.txt ./
# COPY start_container.sh ./
# RUN chmod +x start_container.sh
# RUN pip install -r requirements.txt

# COPY src/ src/
# CMD ["/usr/sbin/sshd","-D"]
