# Using Python Slim-Buster
FROM Indomiee/IndomieUserbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By IndomieUserbot ━━━━━

RUN git clone -b IndomieUserbot https://github.com/indomiegorengsatu/IndomieUserbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/indomiegorengsatu/IndomieUserbot/IndomieUserbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
