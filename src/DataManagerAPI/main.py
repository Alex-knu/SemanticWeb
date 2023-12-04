from flask import Flask, jsonify, request
import os
import gdb_operations as gdb
import  wikidata_museums as wm

app = Flask(__name__)


@app.route('/museum/collection', methods=['GET'])
def get_museums():
    response = gdb.get_all_museums()
    return jsonify(response)


@app.route('/museum', methods=['POST']) #/<string:museum_url>
def get_museum():
    #museum_url = request.args.get('museum_url')

    data = request.json
    print(data['museum_url'])
    response = gdb.get_museum(data['museum_url'])

    return jsonify(response)


@app.route('/synchronize', methods=['POST'])
def add_book():
    status_code1 = gdb.clear_graph()
    if status_code1 != 204:
        return jsonify('Error while clearing graph!'), 500

    try:
        wm.get_museums_from_wikidata()
    except:
        return jsonify('Error while trying to get data from Wikidata!'), 500

    status_code2 = gdb.upload_data()
    if status_code2 != 204:
        return jsonify('Error while uploading data to graph!'), 500

    return jsonify('OK'), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=7777)