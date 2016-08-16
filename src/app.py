from flask import Flask
from greplin import scales
from flask import jsonify
# from flask import abort
# from flask import make_response
# from fflag import FeatureFlag
# from redis.exceptions import ConnectionError
# import random
# import requests
# import sys
# from timeit import default_timer as timer

app = Flask(__name__)


STATS = scales.collection('/web',
    scales.IntStat('errors'),
    scales.IntStat('success'),
    scales.PmfStat('latency'))


@app.route('/api/lists/<listid>')
def get_list():
    with STATS.latency.time():
        obj = {'id':listid, 'taskList':["Task11","Task12"]}
        return jsonify(**obj)

@app.errorhandler(404)
def page_not_found(error):
    return '<h1>No such URL exists</h1>', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')