from configparser import ConfigParser
import socket, errno, logging, time, os
import requests


def wait(host, port):
    """
    Wait for network service to appear
    (adapted from http://code.activestate.com/recipes/576655)
    """
    logging.info("Waiting for server {host}:{port}".format(**locals()))
    with socket.socket() as s:
        while True:
            try:
                s.connect((host, int(port)))
                return
            except:
                logging.exception("Could not connect to {host}:{port}, waiting 1s"
                                  .format(**locals()))
                time.sleep(1)


def wait_http(url, status_codes=(200,)):
    while True:
        try:
            r = requests.get(url)
            if r.status_code in status_codes:
                return
        except Exception as e:
            logging.warning(repr(e))
        
        logging.info("Could not get {url}, waiting 1s".format(**locals()))
        time.sleep(1)

logging.basicConfig(level=logging.INFO, format='[%(asctime)s %(name)-12s %(levelname)-5s] %(message)s')
              
config = ConfigParser()
config.read(['/amcat.ini', '/etc/amcat/amcat.ini', os.path.expanduser('~/.amcat.ini')])
logging.info(config.sections())
wait(host=config.get('database', 'host', fallback='localhost'),
     port=config.get('database', 'port', fallback=5432))

es_host = config.get('elasticsearch', 'host', fallback='localhost')
es_port = config.get('elasticsearch', 'port', fallback=9200)
wait_http('http://{}:{}'.format(es_host, es_port))
