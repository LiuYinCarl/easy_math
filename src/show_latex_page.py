import webbrowser
import re
# 更新建议 使用模板引擎，将HTML和python代码分开


#
# f = open(HTML, 'w')
# message =
#
# f.write(message)
# f.close()
#
# webbrowser.open(HTML, new=1)


def create_html(latex_string):
    """
    将传入的latex 字符串 插入到 HTML 文件中
    :param latex_string: latex 字符串
    :return: None
    """
    HTML = "show_latex_page.html"  # 命名生成的html
    with open(HTML, 'r') as f:
        message = f.read()
    message = message.replace('latex_string', latex_string)

    with open(HTML, 'w') as f:
        f.write(message)
