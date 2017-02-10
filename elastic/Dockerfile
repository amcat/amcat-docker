FROM elasticsearch:2.4

RUN /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head \
    && /usr/share/elasticsearch/bin/plugin install analysis-icu \
    && /usr/share/elasticsearch/bin/plugin install amcat/hitcount/2.4.4

RUN wget -q https://raw.githubusercontent.com/amcat/amcat/master/config/elasticsearch/amcat_remove_from_set.groovy -O /etc/elasticsearch/scripts/amcat_remove_from_set.groovy \
    && wget -q https://raw.githubusercontent.com/amcat/amcat/master/config/elasticsearch/amcat_add_to_set.groovy -O /etc/elasticsearch/scripts/amcat_add_to_set.groovy \
    && wget -q https://raw.githubusercontent.com/amcat/amcat/master/config/elasticsearch/amcat_lead.groovy -O /etc/elasticsearch/scripts/amcat_lead.groovy
