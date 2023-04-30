import requests
import json
from combojsonapi.event.resource import EventsResource
from flask import request, jsonify
from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.configs import API_URL
from blog.schemas import ArticleSchema
from blog.extensions import db
from blog.models import Article


class ArticleListEvent(EventsResource):
    def event_get_count(self, *args, **kwargs):
        return{'count': Article.query.count()}

    def event_get_list(self, *args, **kwargs):
        # return{'list': requests.get('https://flask-api-deployment-cr01.onrender.com/api/articles').json()}
        # return{'list': requests.get(f'{API_URL}/api/articles').json()}
        return{'list': requests.get('http://127.0.0.1:5000/api/articles').json()}  # this works
        # return{'list': Article.query.all()}                              # this don't works
        # return{'list': Article.query.all().json()}                       # this don't works
        # article_set = json.dumps(Article.query.all())
        # return{'list': article_set}


    def event_post_count(self):
        return{'method': request.method}

    def event_get_api_server(self):
        return {'count': requests.get('https://ifconfig.io/ip').text}


class ArticleDetailEvent(EventsResource):
    def event_get_count_by_author(self, *args, **kwargs):
        return{'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }
