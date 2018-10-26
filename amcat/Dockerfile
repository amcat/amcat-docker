FROM amcat/amcat-docker:latest
MAINTAINER Wouter van Atteveldt (wouter@vanatteveldt.com)

# build-args:
#   COMMIT: override commit with a sha, tag or branch. Defaults to 'master'

EXPOSE 8000

# Install apt dependencies
RUN apt-get -qq update && apt-get -q install -y locales antiword unrtf python3-dev libxml2-dev libxslt-dev graphviz pspp r-base python3-lxml python3-amqplib python3-psycopg2 python3-requests python3-pygments git python3 python3-pip postgresql-client-9.5 nodejs-legacy npm \
 && locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Use ADD rather than git clone for better caching
ARG COMMIT=master
ADD https://github.com/amcat/amcat/archive/${COMMIT}.tar.gz amcat.tar.gz

# Install amcat and python dependencies
RUN rm -rf /amcat \
 && mkdir /amcat \
 && tar xzf amcat.tar.gz -C /amcat --strip 1 \
 && rm amcat.tar.gz \
 && pip3 install -e /amcat \
 && echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.rstudio.org'; options(repos = r);" > ~/.Rprofile \
 && Rscript -e "install.packages('rjson')" \
 && cd /amcat \
 && bower --allow-root install

COPY run_amcat.sh wait_services.py create_superuser.py ./

CMD bash run_amcat.sh
