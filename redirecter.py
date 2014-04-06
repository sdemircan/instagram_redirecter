#-*- encoding: utf-8

from settings import *
from flask import Flask
from flask import redirect
from instagram import InstagramAPIError
from media import InstagramMediaLinkHandler

app = Flask(__name__)

@app.route('/resource/<media_id>')
def redirect_resource_url(media_id):
    media_url = media_link_handler.get_resource_url(media_id)
    return redirect(media_url)

@app.route('/media/<media_id>')
def redirect_media_link(media_id):
    media_link = media_link_handler.get_media_link(media_id)
    return redirect(media_link)

@app.errorhandler(InstagramAPIError)
def instagram_api_error(error):
    return "Media not found!", 404

if __name__ == '__main__':
    media_link_handler = InstagramMediaLinkHandler(ACCESS_TOKEN)
    app.run(debug = DEBUG, host = HOST)
