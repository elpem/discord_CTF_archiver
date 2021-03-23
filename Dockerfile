FROM ubuntu

RUN apt update
RUN apt install python3 --yes
RUN apt install python3-pip --yes

RUN pip3 install discord
RUN pip3 install python-dotenv

RUN mkdir /opt/source-code

COPY bot.py /opt/source-code
COPY .env /opt/source-code

ENTRYPOINT python3 /opt/source-code/bot.py