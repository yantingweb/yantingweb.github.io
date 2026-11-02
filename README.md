# Tingzhang Xu · Research & Engineering Portfolio

零依赖的英文静态个人网站，包含 Home、Research、Projects、CV / Resume、About / Contact。所有链接使用相对路径，可部署到 GitHub Pages 根域名或项目子目录。没有第三方字体、统计脚本、表单后端或远程依赖。中文版可在内容确认后另建 `zh/` 页面；本版尚未提供语言切换。

## 本次更新

已结合指定经历库完成个人化内容。先阅读 `CONTENT_REVIEW.md` 了解取舍、资料冲突与发布前仍需确认的事项。目标仓库为 `yantingweb.github.io`，尚未创建或部署。

## 本地查看

需要 Python 3.9 或更新版本。在此 README 所在目录打开终端：

```powershell
python build.py
python -m http.server 8000 --directory site --bind 127.0.0.1
```

浏览器访问 http://127.0.0.1:8000 。按 Ctrl+C 结束服务。也可以直接打开 `site/index.html`，所有页面不依赖 JavaScript。

## 修改内容

1. 编辑 `content.json`：姓名、邮箱、GitHub 链接、学校年级、介绍、研究和工程案例。
2. `research` 和 `projects` 可添加多个对象；每个案例填写背景、个人贡献、技术栈、可验证结果及 HTTPS 链接。
3. 如有可公开的 PDF，放入 `site/assets/`，将 `cv_pdf` / `resume_pdf` 分别填写为 `assets/cv.pdf` / `assets/resume.pdf`。留空会显示待补充，不会出现失效下载按钮。
4. 每次修改后运行 `python build.py`。不要直接修改生成的 HTML，下次构建会覆盖。
5. 布局与配色在 `site/assets/style.css`；页面结构和固定文案在 `build.py`。搜索其中的 pending、awaiting、To be added，补全后再公开。

`reviewed_for_publication: false` 会显示草稿提示、添加 noindex，并阻止部署工作流。**noindex 不是访问控制**，公开仓库中的文件仍可被访问。只有在逐项审核全部文字、链接和附件后才改为 `true`；此开关不会自动核实内容，也不会删除正文中的占位符。

## GitHub Pages 部署

本包已经准备部署配置，尚未连接 GitHub、创建仓库或上线。不要将敏感材料放入待上传目录。

推荐免费方案：用 GitHub Free 创建公开仓库，仓库名为 `你的用户名.github.io`，发布地址为 `https://你的用户名.github.io/`。仓库名也可以是 `portfolio`，对应 `https://你的用户名.github.io/portfolio/`，本模板同样支持。无需购买域名。

1. 创建上述仓库，以 `main` 为默认分支。
2. 在本地完成内容审核，并将 `reviewed_for_publication` 改成 `true`。
3. 上传本目录内容到仓库根目录，包括 `.github/workflows/pages.yml`。推荐使用 GitHub Desktop 添加本目录、提交并发布仓库。不要把外层 `portfolio/` 文件夹再套一层。
4. 在仓库 Settings → Pages → Build and deployment 中选择 **GitHub Actions**。
5. 在 Actions 中打开 **Deploy portfolio to GitHub Pages**，运行工作流；如果首次推送时还没启用 Pages，启用后重新运行。
6. 等工作流成功，在部署记录打开实际网址，检查手机排版、所有链接、邮箱、PDF 和项目证据。

部署只上传 `site/`，README 和构建脚本不会作为网站内容发布，但公开仓库本身仍会公开这些源文件。以后推送到 `main` 会自动更新网站。失败时先看 Actions 日志：内容审核失败需完成审核开关；PDF 路径失败需检查文件实际存在；Pages 权限失败需检查发布源与仓库 Actions 权限。

部署配置依据 GitHub 官方文档：
https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## 内容原则

- 北邮大二、具身智能/机器人方向、RAPID 复现来自本次需求，尚未作为独立事实核验，公开前请确认。
- 未假定 RAPID 的具体论文、作者、任务或算法；请补充原论文链接，避免混淆同名工作。
- 复现不等于原创成果；说明原作者、复现范围、个人修改和评价方法。
- 未发表工作标注 Work in progress；预印本标注 Preprint；仅在正式接收后写 Accepted，正式发表后补齐完整引用。
- 不能用“代码开源”替代成果证明，也不需要为了展示上传闭源代码。经授权的演示、架构图、脱敏报告也可作为证据。
- 避免未经批准的导师/合作方姓名、实验室材料、数据集样本、内部日志、密钥及个人隐私。删除 Git 历史中的文件需要单独处理，不能只删最新文件。

## 文件

`content.json` 内容入口；`build.py` 生成页面；`site/` 可直接发布的网站；`.github/workflows/pages.yml` 部署工作流；`CONTENT_CHECKLIST.md` 待填和发布检查清单。
