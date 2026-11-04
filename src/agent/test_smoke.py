def test_env_ready():
    """冒烟测试：验证整套环境是通的"""
    assert 1 + 1 == 2


def test_package_importable():
    """验证 src 布局 + 可编辑安装正常工作"""
    import agent

    assert agent is not None