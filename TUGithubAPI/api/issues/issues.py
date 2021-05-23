from TUGithubAPI.core.rest_client import RestClient
class Issues(RestClient):
    def create_issue(self,owner,repo,**kwargs):
        return self.post('/repos/{}/{}/issues'.format(owner,repo),**kwargs)