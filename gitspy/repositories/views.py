import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from python_graphql_client import GraphqlClient
import asyncio
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

KEY = env('KEY')
headers = {"Authorization": "Token {}".format(KEY)}
client = GraphqlClient(
    endpoint="https://api.github.com/graphql", headers=headers)

query = """{
    viewer {
        repositories(first: 100) {
            totalCount
            pageInfo {
                endCursor
                hasNextPage
            }
            nodes{
                name
                owner {
                    login
                }
                description
                languages(first: 50) {
                    nodes{
                        name
                        color
                    }
                }
                pushedAt
            }
        }
    }
 }
"""


def index(request):
    data = asyncio.run(client.execute_async(query=query))
    data = data['data']['viewer']['repositories']['nodes']
    # data = data
    string_data = json.dumps(data)
    parsed_data = json.loads(string_data)
    context = {
        'data': data,
        'parsed_data': parsed_data,
        'string_data': string_data
    }
    template = loader.get_template('repositories/index.html')

    return HttpResponse(template.render(context, request))
