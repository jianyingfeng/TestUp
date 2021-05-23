from TUGithubAPI.github import Github
from TUGithubAPI.operations.repo import create_repo

if __name__ == '__main__':
    github = Github('http://api.github.com',token="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")
    # result = create_repo(github,'hasaiki')
    # assert result.success == True,result.error

    # result = create_repo(github,'hasaiki')
    # assert result.success == True,result.error

    repo_name="test_repo_{}"
    result=create_repo(github,repo_name)
    assert result.status_code == 201