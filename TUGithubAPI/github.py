from TUGithubAPI.api.repositories.repos import Repos
from TUGithubAPI.api.git_data.gitdata import GitData
import json
class Github():
    def __init__(self,api_root_url,**kwargs):
        self.api_root_url = api_root_url
        self.repos = Repos(self.api_root_url,**kwargs)
        self.gitdata = GitData(self.api_root_url,**kwargs)

if __name__ == '__main__':
    # r = Github(token='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')
    # x = r.repos.list_your_repos()
    # print(x.url)
    # print(x.text)

    # r = Github('http://api.github.com',token='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')
    # x = r.repos.list_org_repos('TestUpCommunity')
    # print(x.text)


    r = Github(token="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")
    username = "jianyingfeng"
    orgnname = "Janenanfeng"

    # case 1
    data = {
            "name": "Hello-World",
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": False,
            "has_issues": True,
            "has_projects": True,
        "has_wiki": True
    }

    x = r.repos.create_user_repo(json=data)
    print(x.text)

    # # case 2
    # x = r.repos.create_org_repo('Janenanfeng',json=data)
    # print(x.text)

    # case 3
    # y = r.repos.get_repo('Janenanfeng','Hello-World')
    # print(y.text)

    #case 4
    # update_data = {
    #     "name": "Hello-World",
    #     "description": "DDDD:This is your first repository",
    #     "homepage": "https://github.com",
    #     "private": False,
    #     "has_issues": True,
    #     "has_projects": True,
    #     "has_wiki": True
    # }
    #
    # x = r.repos.edit_repo('Janenanfeng','Hello-World',data=json.dumps(update_data))
    # print(x.text)

    # x = r.repos.traffic.list_clones('jianyingfeng','hello')
    # print(x.text)

    # x = r.repos.branches.list_branches('zhangting85','simpleWebtest')
    # print(x.text)

    # r = Github(token="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")
    # username = "zhangting85"
    # orgname = "TestUpCommunity"
    # reponame ="simpleWebtest"
    # # case 1
    # x = r.repos.get_repo(username, reponame)
    # print(x.status_code)
    # assert x.status_code == 200
    # print(x.text)
    # x = r.repos.traffic.list_clones(username, reponame)
    # # assert x.status_code == 200
    # print(x.text)
    # x = r.repos.traffic.statistics.get_numbers_commits_hour(username,reponame)
    # print(x.text)

    # r = Github(token="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")
    # # y = r.repos.get_repo('Janenanfeng','Hello-World')
    # # print(y.text)
    # username = "jianyingfeng"
    # reponame ="hello"
    # x = r.repos.traffic.list_clones(username, reponame)
    # # assert x.status_code == 200
    # print(x.text)