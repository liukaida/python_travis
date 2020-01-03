# python_travis
travis的python实验
[![Build Status](https://travis-ci.org/liukaida/python_travis.svg?branch=master)](https://travis-ci.org/liukaida/python_travis)


将上述过程转换为.travis.yml脚本，添加到Github仓库根目录中:

os: linux
sudo: false
language: python

python:
  - "3.6"
install:
  - pip install -r requirements.txt
  - pip install -r requirements_test.txt
script:
  - nosetests tests
cache:
  - pip
branches:
  only:
    - master

notifications:
  email: false
*重要字段解释：

os: 持续集成运行环境
sudo: 是否以管理员身份运行
language: 代码语言
python: 若language为python，可以在python键下指定具体的python版本
install: 安装依赖
scripts: 执行持续集成的命令，对我这个项目来说，持续集成用于运行单元测试，因此scripts中写执行测试的命令即可
branches: 需要进行持续集成的分支
具体的.travis.yml编写可查看官方文档：https://docs.travis-ci.com/user/getting-started
