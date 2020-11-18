from flask import jsonify
from . import controller

data = {
    "swagger": "2.0",
    "info": {
        "description": "This API can collect datas from sensors",
        "contact": {"email": "apiteam@swagger.io"},
    },
    "host": "api.bai-systems.cf",
    "basePath": "/api",
    "schemes": ["https", "http"],
    "paths": {
        "/apartments": {
            "get": {
                "tags": ["Apartments"],
                "summary": "get All apartments",
                "produces": ["application/json"],
                "responses": [{"200": "success"}]
            }
        },
        "/apartment/{apartment_id}": {
            "get": {
                "tags": ["Apartments"],
                "summary": "Find apartment by id",
                "produces": ["application/json"],
                "parameters": [{
                    "name": "apartment_id",
                    "in": "path",
                    "description": "Id of apartment to return",
                    "required": "true",
                    "type": "integer",
                    "format": "int64"
                }],
                "responses": [{"200": "success"}]
            }
        },
        "/sensors": {
            "get": {
                "tags": ["Sensors"],
                "summary": "get All sensors",
                "produces": ["application/json"],
                "responses": [{"200": "success"}]
            }
        },
        "/sensor/{sensor_id}": {
            "get": {
                "tags": ["Sensors"],
                "summary": "Find sensor by id",
                "produces": ["application/json"],
                "parameters": [{
                    "name": "sensor_id",
                    "in": "path",
                    "description": "Id of sensor to return",
                    "required": "true",
                    "type": "integer",
                    "format": "int64"
                }],
                "responses": [{"200": "success"}]
            }
        },

    }
}


@controller.route('/api/swagger', methods=['GET'])
def get_doc():
    return jsonify(data)
