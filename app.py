from flask import Flask, request
from rpi import set_rgb, cleanup

app = Flask(__name__)

@app.route('/set_rgb')
def set_rgb_route():
    r = request.args.get('r', default=0, type=int)
    g = request.args.get('g', default=0, type=int)
    b = request.args.get('b', default=0, type=int)
    set_rgb(r, g, b)
    return 'OK'

@app.route('/cleanup')
def cleanup_route():
    cleanup()
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
