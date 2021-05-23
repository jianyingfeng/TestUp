import requests

class Response():
    pass

def process(raw_response):
    response = Response()
    response.raw = raw_response
    response.status_code = raw_response.status_code
    try:
        response.content = raw_response.json()
    except:
        response.content = raw_response.content
    return response

class RestClient():
    def __init__(self,api_root_url,username=None,password=None,token=None):
        self.api_root_url = api_root_url
        self.session = requests.session()
        if username and password:
            self.session.auth = (username,password)
        else:
            self.session.headers['Authorization'] = 'token {}'.format(token)

    def get(self,url,**kwargs):
        return process(self.request(url,'get',**kwargs))

    def post(self,url,data=None,json=None,**kwargs):
        return process(self.request(url,'post',data,json,**kwargs))

    def patch(self,url,data=None,**kwargs):
        return process(self.request(url,'patch',data,**kwargs))

    def request(self,url,method,data=None,json=None,**kwargs):
        url = self.api_root_url+url
        if method == 'get':
            return self.session.get(url,**kwargs)
        if method == 'post':
            return self.session.post(url,data,json,**kwargs)
        if method == 'patch':
            # if json:
            #     data = json_pr.dumps(json)
            return self.session.patch(url,data,**kwargs)