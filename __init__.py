
from flask import Flask

from flask import jsonify
from flask import make_response
from flask import request
import json

from BarBeerDrinker import database

app = Flask(__name__)

@app.route('/api/bar', methods =["GET"])
def get_bars():
	return jsonify(database.get_bars())

@app.route("/api/beer", methods=["GET"])
def get_beers():
    try:
        return jsonify(database.get_beers())
    except Exception as e:
        return make_response(str(e), 500)
		
@app.route('/api/drinker', methods =["GET"])
def get_drinkers():
	return jsonify(database.get_drinkers())

@app.route('/api/bar/<name>', methods = ["GET"])
def find_bars(name):
	try:
		if name is None:
			raise ValueError("Bar is not specified.")
		bar = database.find_bar(name)
		if bar is None:
			return make_response("No bar found with the given name.", 404)
		return jsonify(bar)
	except ValueError as e:
		return make_response(str(e), 400)
	except Exception as e:
		return make_response(str(e), 500)

@app.route('/api/beers_cheaper_than', methods = ['POST'])
def find_beers_cheaper_than():
	body = json.loads(request.data)
	max_price = body['maxPrice']
	return jsonify(database.filter_beers(max_price))

@app.route('/api/menu/<name>', methods = ['GET'])
def get_menu(name):
	try:
		if name is None:
			raise ValueError('Bar is not specified.')
		bar= database.find_bar(name)
		if bar is None:
			return make_response("No bar found with the given name.", 404)
		return jsonify(database.get_bar_menu(name))
	except ValueError as e:
		return make_response(str(e), 400)
	except Exception as e:
		return make_response(str(e), 500)

@app.route("/api/beer-manufacturer", methods=["GET"])
def get_beer_manufacturers():
    try:
        return jsonify(database.get_beer_manufacturers(None))
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/beer-manufacturer/<beer>", methods=["GET"])
def get_manufacturers_making(beer):
    try:
        return jsonify(database.get_beer_manufacturers(beer))
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/bartender-tender", methods=["GET"])
def get_tenderName():
    try:
        return jsonify(database.get_tenderName(None))
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/bartender-tender/<bar_name>", methods=["GET"])
def get_Tname(bar_name):
    try:
        return jsonify(database.get_tenderName(bar_name))
    except Exception as e:
        return make_response(str(e), 500)

@app.route("/api/bartender-bar/", methods=["GET"])
def get_BName():
    try:
        return jsonify(database.get_BarName(None))
    except Exception as e:
        return make_response(str(e), 500)


@app.route("/api/bartender-bar/<bar_tender>", methods=["GET"])
def get_BarsName(bar_tender):
	try:
		return jsonify(database.get_BarName(bar_tender))
	except Exception as e:
		return make_response(str(e), 500)


@app.route('/api/bars-selling/<beer>', methods=['GET'])
def find_bars_selling(beer):
    try:
        if beer is None:
            raise ValueError('Beer not specified')
        return jsonify(database.get_bars_selling(beer))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/beer-selling/<beer>', methods=['GET'])
def get_beer_selling(beer):
    try:
        if beer is None:
            raise ValueError('Beer not specified')
        return jsonify(database.get_beer_selling(beer))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/beer-rich/<beer>', methods=['GET'])
def get_Rich(beer):
    try:
        if beer is None:
            raise ValueError('Beer not specified')
        return jsonify(database.get_rich(beer))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/bars-spend/<bar>', methods=['GET'])
def get_top_sepender(bar):
    try:
        if bar is None:
            raise ValueError('Bar not specified')
        return jsonify(database.get_top_sepender(bar))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/bars-beer/<bar>', methods=['GET'])
def get_top_beer(bar):
    try:
        if bar is None:
            raise ValueError('Bar not specified')
        return jsonify(database.get_top_beer(bar))
    except ValueError as e:
        return make_response(str(e), 400)
    except Exception as e:
        return make_response(str(e), 500)


@app.route('/api/frequents-data', methods=['GET'])
def get_bar_frequent_counts():
    try:
        return jsonify(database.get_bar_frequent_counts())
    except Exception as e:
        return make_response(str(e), 500)

@app.route('/api/bartender', methods = ["GET"])
def getTenders():
	return jsonify(database.getTenders())