from TUGithubAPI.core.rest_client import RestClient
from TUGithubAPI.api.repositories.statistics import Statistics
class Traffic(RestClient):
    def __init__(self,api_root_url,**kwargs):
        super(Traffic,self).__init__(api_root_url,**kwargs)
        self.statistics = Statistics(api_root_url,**kwargs)

    def list_clones(self,owner,repo,**kwargs):
        return self.get('/repos/{}/{}/traffic/clones'.format(owner,repo),**kwargs)