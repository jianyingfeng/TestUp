from TUGithubAPI.operations.repo import create_repo,create_branch
from random import randint
import pytest

def test_create_branch_success(env):
    repo_name = 'test_repo_jyf_{}'.format(randint(1,100))
    r = create_repo(env.github,repo_name)
    assert r.success == True,r.error
    r = create_branch(env.github,'jianyingfeng',repo_name,'main','jjj')
    assert r.success == True,r.error

if __name__ == '__main__':
    pytest.main(['-v','-s'])