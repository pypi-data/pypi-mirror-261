import os


def get_env(name: str, default: str = None) -> str:
    """
    获取环境变量.
    :param name: 环境变量名称.
    :param default: 如果为空的默认值.
    :return: 字符串类型的环境变量值.
    """
    return os.environ[name] if name in os.environ else default


def is_github_ci() -> bool:
    """
    判断当前环境是否是Github Actions.
    :return: 是否处在CI环境.
    """
    return 'CI' in os.environ
