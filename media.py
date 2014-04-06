#-*- encoding: utf-8 -*-

from instagram import *

class InstagramMediaLinkHandler:

    def __init__(self, access_token):
        self.access_token = access_token
        self.instagram_api = InstagramAPI(access_token=self.access_token)

    def get_resource_url(self, media_id):
        media = self.instagram_api.media(media_id=media_id)
        resource = media.videos if hasattr(media, 'videos') else media.images

        return resource['standard_resolution'].url

    def get_media_link(self, media_id):
        media = self.instagram_api.media(media_id=media_id)

        return media.link
