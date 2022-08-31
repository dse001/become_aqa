def test_check_repos_can_be_found(git_hub_api_client):
    #git_hub_api_client.get_repos('become-qa-auto')
    repos = git_hub_api_client.get_repos('become-qa-auto')

    assert repos['total_count'] != 0
    assert len(repos['items']) != 0

def test_check_repos_can_not_be_found(git_hub_api_client):
    #git_hub_api_client.get_repos('become-qa-auto')
    repos = git_hub_api_client.get_repos('fghrtretyghfjhgfjjgawf5h4343422vf')
    print(repos)

    assert repos['total_count'] ==0
    assert len(repos['items']) ==0
