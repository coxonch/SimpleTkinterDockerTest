FROM python:3.10

WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "./app.py" ]

## Needed to run GUI, run this in separate terminal
# https://cntnr.io/running-guis-with-docker-on-mac-os-x-a14df6a76efc
# > brew install socat
# > socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"