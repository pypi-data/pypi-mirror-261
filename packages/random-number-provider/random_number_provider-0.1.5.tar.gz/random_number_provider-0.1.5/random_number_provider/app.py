#!/usr/bin/env python
import argparse
import logging
import logging.handlers
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
import xmlschema

from xmlschema import XMLSchema
from flask import Flask, Response, request
from werkzeug.exceptions import HTTPException, NotFound, Unauthorized
from random import randrange

from random_number_provider import __version__

TOKEN = "61665F7F34765E5E27CF2AD483369"

FORMAT = "[%(asctime)s][%(levelname)s][%(name)s]: %(message)s"
FILE_DIR = Path(__file__).parent

flask_app = Flask(__name__)


@flask_app.errorhandler(HTTPException)
def handle_exception(e: HTTPException):
    response = e.get_response()
    root_element = ET.Element("HTTPError")
    ET.SubElement(root_element, "Code").text = str(e.code)
    ET.SubElement(root_element, "Name").text = e.name
    ET.SubElement(root_element, "Name").text = e.description
    ET.indent(root_element, space="\t", level=0)
    response.data = ET.tostring(root_element, encoding='utf8', method='xml')
    response.content_type = "application/xml"
    return response


@flask_app.errorhandler(xmlschema.validators.exceptions.XMLSchemaValidationError)
def handle_exception(e: xmlschema.validators.exceptions.XMLSchemaValidationError):
    root_element = ET.Element("XMLSchemaValidationError")
    ET.SubElement(root_element, "Name").text = "xmlschema.validators.exceptions.XMLSchemaValidationError"
    ET.SubElement(root_element, "Reason").text = e.reason
    ET.indent(root_element, space="\t", level=0)

    return Response(ET.tostring(root_element, encoding='utf8', method='xml'), mimetype="application/xml")


@flask_app.errorhandler(ET.ParseError)
def handle_exception(e: ET.ParseError):
    root_element = ET.Element("ParseError")
    ET.SubElement(root_element, "Name").text = "xml.etree.ElementTree.ParseError"
    ET.SubElement(root_element, "Reason").text = e.msg
    ET.indent(root_element, space="\t", level=0)

    return Response(ET.tostring(root_element, encoding='utf8', method='xml'), mimetype="application/xml")


@flask_app.route("/random_numbers", methods=['POST'])
def random_numbers():
    logging.debug("Request headers: %s", request.headers)
    logging.debug("Request data: %s", request.data)

    provided_token = request.headers["Authorization"]
    if provided_token != f"Bearer {TOKEN}":
        raise Unauthorized

    schema = XMLSchema(FILE_DIR / "xsd/random_numbers_request.xsd")
    schema.validate(request.data)

    request_root_elem = ET.fromstring(request.data)

    response_root_elem = ET.Element("RandomNumbersResponse")

    for random_numbers_request in request_root_elem:
        request_min = int(random_numbers_request.attrib["min"])
        request_max = int(random_numbers_request.attrib["max"])
        request_count = int(random_numbers_request.attrib["count"])

        random_numbers_elem = ET.SubElement(response_root_elem, "RandomNumbers")
        random_numbers_elem.set("min", str(request_min))
        random_numbers_elem.set("max", str(request_max))
        random_numbers_elem.set("count", str(request_count))

        for _ in range(request_count):

            random_number = randrange(request_min, request_max)

            ET.SubElement(random_numbers_elem, "RandomNumber").text = str(random_number)

    ET.indent(response_root_elem, space="\t", level=0)

    return Response(ET.tostring(response_root_elem, encoding='utf8', method='xml'), mimetype="application/xml")


@flask_app.route("/version")
def version():
    root_element = ET.Element("Version")
    root_element.set("value", __version__)
    ET.indent(root_element, space="\t", level=0)
    return Response(ET.tostring(root_element, encoding='utf8', method='xml'), mimetype="application/xml")


@flask_app.route("/")
def index():
    raise NotFound


def start():

    parser = argparse.ArgumentParser(usage="random_number_provider")

    parser.add_argument(
        "-vv",
        "--verbose",
        help="Run with verbose output.",
        action='store_true',
    )

    parser.add_argument(
        "--port",
        help="Set web server port (Default = 50000).",
        type=int,
        default=50000
    )

    parser.add_argument(
        "--host",
        help="Host to listen on (Default = 0.0.0.0).",
        type=str,
        default="0.0.0.0"
    )

    args = parser.parse_args(sys.argv[1:])

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(stream=sys.stdout, format=FORMAT, level=log_level, force=True)
    logging.info("Random number provider started!")
    logging.info("Log level: %s", logging.getLevelName(log_level))

    flask_app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    start()
