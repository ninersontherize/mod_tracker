from flask import Flask, jsonify
from flask_cors import CORS

#config
DEBUG = True

#initialize app
app = Flask(__name__)
app.config.from_object(__name__)

#enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

#ping test route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

MODS = [
    {
        'section': 'wheels',
        'part_name': 'Volk Racing TE37 18-inch',
        'link': 'https://www.systemmotorsports.com/collections/fk8-civic-type-r-wheel-fitment-2017/products/rays-volk-te37-saga-18x9-5-33-5x120-face-4-concave-2017-civic-type-r-fk8-fitment',
        'price': '$3,473.20',
        'purchased': False,
        'installed': False
    },
    {
        'section': 'tires',
        'part_name': 'Michelin Pilot Sport Cup 2',
        'link': 'https://www.tirerack.com/tires/tires.jsp?tireMake=Michelin&tireModel=Pilot+Sport+Cup+2',
        'price': '$1,569.12',
        'purchased': False,
        'installed': False
    },
    {
        'section': 'tires',
        'part_name': 'Pirelli P Zero Trofeo R',
        'link': 'https://www.tirerack.com/tires/tires.jsp?tireMake=Pirelli&tireModel=P+Zero+Trofeo+R&partnum=44YR8P0TRXL&vehicleSearch=true&fromCompare1=yes&autoMake=Honda&autoYear=2021&autoModel=Civic%20Type%20R&autoModClar=',
        'price': '$1,208.80',
        'purchased': False,
        'installed': False
    },
    {
        'section': 'wheels',
        'part_name': 'Volk Racing ZE40 RW LIMITED 18X10',
        'link': 'https://www.systemmotorsports.com/collections/fk8-civic-type-r-wheel-fitment-2017/products/rays-volk-racing-ze40-rw-limited-18x10-36-5x120-4-wheels',
        'price': '$3,350.00',
        'purchased': False,
        'installed': False
    }
]

@app.route('/mods', methods=['GET'])
def all_mods():
    return jsonify({
        'status': 'success',
        'mods': MODS
    })

if __name__ == '__main__':
    app.run()