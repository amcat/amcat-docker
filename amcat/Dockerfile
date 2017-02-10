# This is a comment
FROM ubuntu:16.04
MAINTAINER Wouter van Atteveldt (wouter@vanatteveldt.com)
EXPOSE 8000

# Install apt dependencies. Note: get nodejs immediately as well?
RUN apt-get -qq update && apt-get install -y antiword unrtf python3-dev libxml2-dev libxslt-dev graphviz pspp r-base python3-lxml python3-amqplib python3-psycopg2 python3-requests python3-pygments git python3 python3-pip postgresql-client-9.5

# Install amcat and python dependencies
RUN git clone https://github.com/amcat/amcat /amcat && pip3 install -e /amcat # redo2

# Install R libraries
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile && Rscript -e "install.packages('rjson')"

# Install static files
RUN apt-get install -y nodejs-legacy npm && npm install -g bower && cd /amcat && bower --allow-root install

CMD bash /etc/amcat/run_amcat.sh
