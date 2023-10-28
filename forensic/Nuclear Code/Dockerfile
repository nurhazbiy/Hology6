FROM ubuntu:22.04

# Update the system
RUN apt-get update && apt-get upgrade -y

# Install OpenSSH Server
RUN apt-get install -y openssh-server

# Set up configuration for SSH
RUN mkdir /var/run/sshd
# RUN echo 'root:cool_password' | chpasswd
# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN useradd  -ms /bin/bash hology6

# SSH login fix. Otherwise, user is kicked off after login
# RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

USER hology6
RUN ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519

# WORKDIR /home/hology6
RUN  mkdir -p /home/hology6/.ssh && \
    chmod 0700 /home/hology6/.ssh
RUN touch /home/hology6/.ssh/authorized_keys
COPY key/id_rsa.pub /home/hology6/.ssh/
# RUN ssh-keygen -A
# RUN  chmod 600 /home/hology6/.ssh/id_rsa && \
#     chmod 600 /home/hology6/.ssh/id_rsa.pub
RUN PUBKEY=$(cat /home/hology6/.ssh/id_rsa.pub); grep -q "$PUBKEY"  /home/hology6/.ssh/authorized_keys || echo "$PUBKEY" >> /home/hology6/.ssh/authorized_keys

RUN mkdir /home/hology6/tugas
RUN echo "I'm not a sinfull man xD" >>/home/hology6/tugas/nuclear-code.txt
COPY public /etc/nuclear-code/

USER root

# Expose the SSH port
EXPOSE 22

# Run SSH
CMD ["/usr/sbin/sshd", "-D"]