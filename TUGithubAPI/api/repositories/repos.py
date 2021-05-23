from TUGithubAPI.core.rest_client import RestClient
from TUGithubAPI.api.repositories.traffic import Traffic
from TUGithubAPI.api.issues.issues import Issues
from TUGithubAPI.api.repositories.branches import Branches
class Repos(RestClient):
    def __init__(self, api_root_url, **kwargs):
        self.api_root_url = api_root_url
        super(Repos, self).__init__(self.api_root_url, **kwargs)
        # self.branches = Branches(api_root_url,**kwargs)

    def list_all_public_repos(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-all-public-repositories
        """
        return self.get("/repositories", **kwargs)

    def list_your_repos(self,**kwargs):
        return self.get('/user/repos',**kwargs)

    def list_organization_repos(self, org, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-organization-repositories
        :param org: orgnization name
        """
        return self.get("/orgs/{}/repos".format(org), **kwargs)

    def create_user_repo(self,**kwargs):
        return self.post('/user/repos',**kwargs)

    def create_org_repo(self,org,**kwargs):
        return self.post('/orgs/{}/repos'.format(org),**kwargs)

    def get_repo(self,owner,repo,**kwargs):
        return self.get('/repos/{}/{}'.format(owner,repo,**kwargs))

    def edit_repo(self,owner,repo,**kwargs):
        return self.patch('/repos/{}/{}'.format(owner,repo),**kwargs)