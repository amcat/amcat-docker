from configparser import ConfigParser
import socket, errno, logging, time, os, sys
import requests
import datetime
import signal

TIMEOUT = datetime.timedelta(minutes=3)

class Timeout(Exception):
    pass

def timeout(signum, frame):
    raise Timeout("Timed out trying to connect to services.")

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
            except OSError as e:
                logging.exception("Could not connect to {host}:{port}, waiting 1s"
                                  .format(**locals()))
                time.sleep(1)


def wait_http(url, status_codes=(200,)):
    while True:
        try:
            r = requests.get(url)
            if r.status_code in status_codes:
                return
        except IOError as e:
            logging.warning(repr(e))

        logging.info("Could not get {url}, waiting 1s".format(**locals()))
        time.sleep(1)



if __name__ == "__main__":
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(int(TIMEOUT.total_seconds()))
    try:
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s %(name)-12s %(levelname)-5s] %(message)s')

        config = ConfigParser()
        config.read(['/amcat.ini', '/etc/amcat/amcat.ini', os.path.expanduser('~/.amcat.ini')])
        logging.info(config.sections())
        wait(host=config.get('database', 'host', fallback='localhost'),
             port=config.get('database', 'port', fallback=5432))

        es_host = config.get('elasticsearch', 'host', fallback='localhost')
        es_port = config.get('elasticsearch', 'port', fallback=9200)
        wait_http('http://{}:{}'.format(es_host, es_port))
    except Timeout:
        raise

    signal.alarm(0)
