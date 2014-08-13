#!/usr/bin/python3
import logging
import json

from bottle import route, run, response, abort, post, request

api_version = "1" #API version, please iterate every time you push a version

@route('/')
def root():
    return "HSSPKA API " + api_version