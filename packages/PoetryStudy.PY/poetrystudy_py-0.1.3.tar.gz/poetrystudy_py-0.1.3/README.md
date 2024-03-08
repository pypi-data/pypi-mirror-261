# 说明

1. 安装poetry:`pip install poetry`(除了第一次安装poetry，其他时候均使用`poetry`命令代替`pip`命令)
2. 新建poetry项目:`poetry new myproject`,如果是既有项目要加入poetry，请使用:`poetry init`
3. 安装依赖:`poetry add XXX`
   如果被依赖的项目有特殊符号，可以使用双引号包裹起来，比如`poetry add "BasicLibrary.PY"`
   （安装依赖类库也可以通过手工修改`pyproject.toml`文件，然后执行`poetry update`得到同样效果）
4. 打包:`poetry build`
5. 发布:`poetry publish`（需要先注册pypi网站的账户,并配置token。具体参见下面说明）





## 其他说明：
1. 更换国内类库源：
   在`pyproject.toml`文件中，找到`[tool.poetry.source]`，修改`default`为`https://mirrors.aliyun.com/pypi/simple/`
2. 配置发布平台pypi的token
   1. 登录pypi网站，点击右上角头像，选择`Settings`
   2. 选择`Access`，然后点击`Generate token`
   3. 输入`Token description`，然后点击`Generate token`
   4. 复制生成的token，配置在poetry的工具本身的配置文件中，如下：
      配置PyPI令牌: 可以通过 poetry config pypi-token.pypi <token> 命令配置PyPI令牌，以便在发布包时不需要手动输入用户名和密码。
   5. 发布：`poetry publish`
