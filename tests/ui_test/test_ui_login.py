from applications.ui.pages.PageLogin import PageLogin
from providers.user_providers import UserProvider

#homework v2!

def test_ui_login_fall(ui_github):
    ui_github.login(username=UserProvider.user_data['fakeusername'], userpassword=UserProvider.user_data['fakeusername'])
    assert ui_github.error_login() == 'Incorrect username or password.'
