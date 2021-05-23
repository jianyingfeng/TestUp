from TUGithubAPI.core.rest_client import RestClient
class Branches(RestClient):
    def list_branches(self,owner,repo,**kwargs):
        return self.get('/repos/{owner}/{repo}/branches',**kwargs)