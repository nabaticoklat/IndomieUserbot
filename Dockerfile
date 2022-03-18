FROM vckyouuu/geezproject:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By IndomieUserbot ━━━━━

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

RUN git clone -b IndomieUserbot https://github.com/IndomieGorengSatu/IndomieUserbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/IndomieGorengSatu/IndomieUserbot/IndomieUserbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
