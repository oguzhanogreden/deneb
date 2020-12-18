FROM python:3.9-buster

ADD https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_77.0.3865.120-1_amd64.deb /chrome.deb 
ADD https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip /chromedriver_linux64.zip

RUN set -ex \
    && apt-get -y update \
    && unzip /chromedriver_linux64.zip -d /usr/local/bin \
    && chmod +x /usr/local/bin/chromedriver \
    && dpkg -i /chrome.deb || apt-get install -fy \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm /chrome.deb \
    && rm /chromedriver_linux64.zip

ADD requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "-m", "deneb"]

CMD ["--help"]
