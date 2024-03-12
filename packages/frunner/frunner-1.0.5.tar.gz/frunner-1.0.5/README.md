# FRunner

FRunner is Full stack automated testing framework

`FRunner` This package exists to provide One-stop solution for HTTP(S) automated testing, that can be used to aotumated testing in your next Python project. Supporting platforms: Web、Api、Android、IOS、H5、windows、mac.

## 部署

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple frunner

allure安装：https://github.com/allure-framework/allure2/releases

- windows: 下载allure的zip包，解压到本地后配置环境变量
- mac：brew命令安装：/usr/bin/ruby -e "$(curl -fsSL https://cdn.jsdelivr.net/gh/ineo6/homebrew-install/install)"（brew install allure）

## 运行

python run.py


安装成功后，你将获得一个 `frun/frunner` 命令行工具
- `frun -V` 即可查看版本信息
- `frun -h` 即可查看到参数帮助说明
- `frun startproject -t api -n api_project` 即可生成测试项目（t:平台, -n:项目名称; 支持api、android、ios、web）