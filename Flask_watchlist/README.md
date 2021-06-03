# 我的Flask练习项目
创建远程仓库
访问新建仓库页面（导航栏“+” - New repository），在“Repository name”处填写仓库名称，这里填“watchlist”即可，接着选择仓库类型（公开或私有）等选项，最后点击“Create repository”按钮创建仓库。
因为我们已经提前创建了本地仓库，所以需要指定仓库的远程仓库地址：
$ git remote add origin git@github.com:greyli/watchlist.git  # 注意更换地址中的用户名
这会为本地仓库关联一个名为“origin”的远程仓库，注意将仓库地址中的“greyli”换成你的 GitHub 用户名。
如果还没有创建本地仓库，则可以直接将远程仓库克隆到本地（这会在当前目录创建一个名为 watchlist 的文件夹）：
$ git clone git@github.com:greyli/watchlist.git  # 注意更换地址中的用户名

创建虚拟环境
`python3 -m venv env`
激活虚拟环境
`env\Scripts\activate #windows` 
`. env/bin/activate  # Linux 或 macOS` 
退出虚拟环境
`deactivate` \n


Flask 是典型的微框架，作为 Web 框架来说，它仅保留了核心功能：请求响应处理和模板渲染。这两类功能分别由 Werkzeug（WSGI 工具库）完成和 Jinja（模板渲染库）完成，因为 Flask 包装了这两个依赖，我们暂时不用深入了解它们。