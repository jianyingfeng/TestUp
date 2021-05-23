from TUGithubAPI.api.repositories.repos import Repos
from TUGithubAPI.core.base import CommonItem
def create_repo(github,name,org=None,description=None, homepage=None, private=False, has_issues=True,
                has_projects=True, has_wiki=True,auto_init=True):
    result = CommonItem()
    payload = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "auto_init": auto_init
    }

    result.success = False
    if org:
        response = github.repos.create_org_repo(org=org,json=payload)
    else:
        response = github.repos.create_user_repo(json=payload)
    result.response = response
    if response.status_code == 201:
        result.success = True
    else:
        result.error = 'create repo got {},should be 201'
    return result

# def create_branch(github,owner,repo,source_branch_name,new_branch_name):
#     result = CommonItem()
#     result.success = True
#     result.error = None
#     response = github.gitdata.refs.get_a_reference(owner,repo,source_branch_name)
#     if response.status_code != 200:
#         result.success = False
#         result.error = 'get a reference failed,status_code should be 200,but got {}'.format(response.status_code)
#         result.response = response
#         return result
#     sha = response.content['object']['sha']
#     pay_load = {
#     "ref": "refs/heads/{}".format(new_branch_name),
#     "sha": sha
#     }
#     response = github.gitdata.refs.create_a_reference(owner,repo,json=pay_load)
#     result.success = True
#     result.error = None
#     if response.status_code != 201:
#         result.success = False
#         result.error = 'create_a_reference failed,status_code should be 201,but got {}'.format(response.status_code)
#         result.response = response
#         return result
#     result.response = response
#     return result

def create_branch(github,owner,repo,source_branch_name,new_branch_name):
    result = CommonItem()
    result.success = False
    response = github.gitdata.refs.get_a_reference(owner,repo,source_branch_name)
    result.response = response
    if response.status_code == 200:
        result.success = True
    else:
        result.error = 'got source branch sha fails,repo={} got {},should be 200'.format(repo,response.status_code)
    source_branch_sha = response.content['object']['sha']
    payload = {
        "ref": "refs/heads/{}".format(new_branch_name),
        "sha": source_branch_sha
    }
    response = github.gitdata.refs.create_a_reference(owner,repo,json=payload)
    result.success = False
    result.response = response
    if response.status_code == 201:
        result.success = True
    else:
        result.error = 'create branch fails,repo={} got {},should be 201'.format(repo, response.status_code)
    return result