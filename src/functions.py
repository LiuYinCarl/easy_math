import os


def get_abs_path():
    """
    @brief: 获取当前绝对位置
    :return: 当前绝对位置（unix格式）
    """
    return os.getcwd().replace('\\', '/')

