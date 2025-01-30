from app import app, db
from flask import request, jsonify
from models import URI
import utils

@app.route('/api/short', methods=["POST"])
def generate_uri():
    try:
        # Get JSON data from request
        data = request.json
        uri = data.get('uri')
        custom = data.get('customUri')
        
        # Check if required fields are provided
        exist = URI.query.all()
        if custom in [i.short_uri for i in exist]:
            return jsonify({'error': 'choose a unique short url to continue'}), 400
        
        if not uri:
            return jsonify({'error': 'missing required fields'}), 400
        
        # Assign random insult if customUri not provided
        if not custom:
            custom = utils.generate_insult()
            print(custom)
        print(custom)
        # Create a new URI entry and add it to the database
        new_uri = URI(short_uri=custom, main_uri=uri)
        db.session.add(new_uri)
        db.session.commit()
        
        # result = [new_uri.serialize_json()]
        
        # Serialize the URI and return the result
        return jsonify( {
        'id': new_uri.id,
        'shortUri': new_uri.short_uri,
        'main_uri': new_uri.main_uri
    }), 201

    except Exception as e:
        # Rollback in case of error and return error message
        db.session.rollback()
        print(f"Error: {e}")  # Log the error for debugging
        return jsonify({'error': 'an unexpected error occurred', 'msg': str(e)}), 500
    

@app.route('/api/all', methods=["GET"])
def get_uri():
    try:
        uris = URI.query.all()
        
        if len(uris) == 0:
            return jsonify({'error': 'no data for this user'}), 404
        
        result = [uri.serialize_json() for uri in uris]
        
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'An error occured'}, str(e)), 401
    

@app.route('/api/<string:uri>', methods=["POST"])
def redirect_incoming_request(uri):
    try:
        uris = URI.query.all()
        
        ltr = [item.short_uri for item in uris]  
        
        if uri not in ltr:
            return jsonify({"msg": "Item Not Found"}), 404  

        found_uri = URI.query.filter_by(short_uri=uri).first()

        if not found_uri:  
            return jsonify({"msg": "Item Not Found"}), 404

        return jsonify(found_uri.serialize_json())
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred", "msg": str(e)}), 500

        
