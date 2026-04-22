import time
import redis
from flask import Flask

app = Flask(__name__)
# Se conecta al servicio 'cache_db' definido en el docker-compose
cache = redis.Redis(host='cache_db', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'¡Hola Orlando! Esta página se ha visto {count} veces.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
