# -*- coding:utf-8 -*-
import os.path
import sys

api_run_content = """import frunner


if __name__ == '__main__':
    frunner.main(
        platform='api',
        base_url='https://www.qizhidao.com'
    )
"""

android_run_content = """import frunner


if __name__ == '__main__':
    frunner.main(
        platform='android',
        serial_no='UJK0220521066836',
        pkg_name='com.qizhidao.clientapp'
    )
"""

ios_run_content = """import frunner


if __name__ == '__main__':
    frunner.main(
        platform='ios',
        serial_no='00008101-000E646A3C29003A',
        pkg_name='com.qizhidao.company'
    )
"""

browser_run_content = """import frunner


if __name__ == '__main__':
    frunner.main(
        platform='web',
        base_url='https://patents-pre.qizhidao.com'
    )
"""

case_content_android = """from frunner import *
from frunner.core.android import *


@story('首页')
class TestAdrSample(TestCase):
    
    @title('从首页进入我的页')
    def test_go_my(self):
        self.click(resourceId='id/bottom_btn', desc='广告关闭按钮')
        self.click(resourceId='id/bottom_view', index=3, desc='底部导航-我的')
        self.assertText('我的订单')
"""

case_content_ios = """from frunner import *
from frunner.core.ios import *


@story('首页')
class TestIosSample(TestCase):

    @title('从首页进入我的页')
    def test_go_my(self):
        self.click(label='我的', desc='底部导航-我的')
        self.assertText('我的订单')
"""

case_content_web = """from frunner import *
from frunner.core.web import *


@story('专利检索')
class TestWebSample(TestCase):
    
    @title('专利简单检索')
    def test_patent_search(self):
        self.open_url('https://patents-pre.qizhidao.com/', desc='专利首页')
        self.input('无人机', id_="driver-home-step1", desc='专利搜索框')
        self.click(id_='driver-home-step2', desc='搜索按钮')
        self.assertTitle('无人机专利检索-企知道')
"""

case_content_api = """from frunner import *
from frunner.core.api import *


@story('PC站首页')
class TestApiSample(TestCase):

    @title('查询PC站首页banner列表')
    @file_data('card_type', 'data.json')
    def test_getToolCardListForPc(self, card_type):
        path = '/api/qzd-bff-app/qzd/v1/home/getToolCardListForPc'
        load = {"type": card_type}
        self.post(path, json=load)
        self.assertEq('code', 0)
"""

require_content = """frunner
"""

ignore_content = "\n".join(
    ["__pycache__/*", "*.pyc", ".idea/*", ".DS_Store", "allure-results", "report"]
)

data_content = """{
  "card_type": [0, 1, 2]
}
"""


def init_scaffold_project(subparsers):
    parser = subparsers.add_parser("startproject", help="Create a new project with template structure.")
    parser.add_argument('-t', '--platform', dest='platform', type=str, default='api', help='测试平台: api、android、ios、web')
    parser.add_argument('-n', '--name', dest='project_name', type=str, help='项目名称')
    return parser


def create_scaffold(platform, project_name):
    """ create scaffold with specified project name.
    """

    def create_folder(path):
        os.makedirs(path)
        msg = f"created folder: {path}"
        print(msg)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)
        msg = f"created file: {path}"
        print(msg)

    if not project_name:
        project_name = f'{platform}_demo'
    project_name = project_name
    create_folder(project_name)
    create_file(
        os.path.join(project_name, ".gitignore"),
        ignore_content,
    )
    create_file(
        os.path.join(project_name, "requirements.txt"),
        require_content,
    )
    create_folder(os.path.join(project_name, 'test_dir'))
    create_folder(os.path.join(project_name, 'test_data'))
    create_folder(os.path.join(project_name, 'test_dir', 'common'))
    create_folder(os.path.join(project_name, 'test_dir', 'test_case'))
    create_file(
        os.path.join(project_name, 'test_dir', "__init__.py"),
        '',
    )
    create_file(
        os.path.join(project_name, 'test_dir', 'test_case', "__init__.py"),
        '',
    )
    create_file(
        os.path.join(project_name, 'test_dir', 'common', "__init__.py"),
        '',
    )
    create_file(
        os.path.join(project_name, 'test_data', "data.json"),
        data_content,
    )
    if platform == 'api':
        create_file(
            os.path.join(project_name, "run.py"),
            api_run_content,
        )
        create_file(
            os.path.join(project_name, 'test_dir', 'test_case', "test_api_sample.py"),
            case_content_api,
        )
    elif platform == 'android':
        create_file(
            os.path.join(project_name, "run.py"),
            android_run_content,
        )
        create_file(
            os.path.join(project_name, 'test_dir', 'test_case', "test_adr_sample.py"),
            case_content_android,
        )
    elif platform == 'ios':
        create_file(
            os.path.join(project_name, "run.py"),
            ios_run_content,
        )
        create_file(
            os.path.join(project_name, 'test_dir', 'test_case', "test_ios_sample.py"),
            case_content_ios,
        )
    elif platform == 'web':
        create_file(
            os.path.join(project_name, "run.py"),
            browser_run_content,
        )
        create_file(
            os.path.join(project_name, 'test_dir', 'test_case', "test_web_sample.py"),
            case_content_web,
        )
    else:
        print(f'不支持的平台: {platform}')
        sys.exit()
    return 0


def main_scaffold_project(args):
    print("------scaffold------")
    sys.exit(create_scaffold(args.platform, args.project_name))

