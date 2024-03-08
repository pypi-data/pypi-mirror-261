# 说明：
## 项目结构的推荐格式

```shell
tree ./ ./ 
├── LICENSE 
├── README.md 
├── pyproject.toml 
├── src 
│ └── npts # src 下面是包名，包下面是业务代码 
│      ├── __init__.py 
│      └── core.py 
└── tests 3 directories, 5 files
```

## pyproject.toml的说明
1. Python从PEP 518开始引入的使用pyproject.toml管理项目元数据的方案。

2. 该方案已被大多数Python项目采用，并作为PEP 621的实现。

3. pyproject.toml文件用于定义项目的元数据，例如依赖项、版本号等。

4. 该文件应放置在项目的根目录下，并使用特定的语法和结构。

5. 可以使用第三方工具或库（如pip、setuptools等）来解析和处理pyproject.toml文件。

6. 该方案已被证明是管理Python项目的有效方式，并已成为标准。

### 示例：
```shell
[tool.poetry]
name = "your-project-name"
version = "0.1.0"
description = "A short description of your project"
authors = ["Your Name <you@example.com>"]
dependencies = [
    "requests",
    "python-dotenv"
]
[tool.poetry.dependencies]
requests = "^2.28.1"
python-dotenv = "^0.19.2"
[tool.poetry.dev-dependencies]
pytest = "^6.2.5"
flake8 = "^4.0.1"
[project]
name = "your-project-name"
version = "0.1.0"
description = "A short description of your project"
authors = ["Your Name <you@example.com>"]
dependencies = [
    "requests",
    "python-dotenv"
]
[project.scripts]
test = "pytest"
[tool.poetry.scripts]
my-script = "path.to.script:main"
[tool.poetry.build]
requires = ["wheel"]
command = "poetry build"
[tool.poetry.publish]
command = "poetry publish"  
```

