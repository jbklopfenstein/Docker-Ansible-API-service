FROM python:2.7.16-stretch
LABEL MAINTAINER jklopfen@cisco.com
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# Install Ansible - used a known working version that still supports the ansible ios_config module
RUN apt update
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN apt update

# pip package mgr allows ansible version specification
RUN pip install ansible==2.4.2.0

RUN pip install git+https://gitscm.cisco.com/scm/esp-snow/esp-snow-lib-py.git && pip install -r requirements.txt
COPY . /app

# Add playbook role directory dependencies
# playbook yaml will upload to uploads/
# tasks yaml will upload to uploads/roles/tasks/
# Vars yaml will upload to uploads/roles/vars/ 
RUN mkdir -p /app/uploads/roles/change_transitcsr_config/tasks/
RUN mkdir /app/uploads/roles/change_transitcsr_config/vars/
RUN mkdir /app/results
RUN mkdir /root/.ssh

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
