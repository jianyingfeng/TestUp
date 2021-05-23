import pytest
def test_list_all_public_repos(env):
    r = env.github.repos.list_all_public_repos()
    print(r)
    assert r.status_code == 200,'status_code should be 200,not {}'.format(r.status_code)
    assert r.content[0]["id"] == 1
    assert r.content[0]["name"] == "grit"
    assert r.content[0]["private"] == False

def test_list_organization_repos_num(env):
    r = env.github.repos.list_organization_repos('TestUpCommunity')
    assert r.status_code == 200, 'status_code should be 200,not {}'.format(r.status_code)
    assert len(r.content) == 5

def test_list_organization_repos_name(env):
    r = env.github.repos.list_organization_repos('TestUpCommunity')
    assert r.status_code == 200, 'status_code should be 200,not {}'.format(r.status_code)
    assert r.content[0]['name'] == 'TUGithubAPI'
    assert r.content[1]['name'] == 'TUGithubAPITest'

if __name__ == '__main__':
    pytest.main()