# 许庭彰 · 个人作品集

网站：https://yantingweb.github.io/

中文主站面向技术招聘与科研申请，英文入口位于 en/。包含首页、项目、科研、可打印简历和联系页。

## 修改与预览

需要 Python 3.9+，无第三方依赖。在本目录运行：

```powershell
python build.py
python -m http.server 8000 --directory site --bind 127.0.0.1
```

打开 http://127.0.0.1:8000 。Ctrl+C 停止服务。

- content-zh.json：中文项目内容，首页显示前三项。
- content.json：英文资料及共用联系方式；reviewed_for_publication 控制部署审核开关。
- build.py / build_en.py：中英文页面生成。
- site/assets/recruit.css：中文站和打印样式。
- site/assets/style.css：英文站与基础样式。

修改后重新构建，不要直接编辑生成的 HTML。构建同步 site/ 和根目录，以兼容 Actions 与 main 根目录发布。

## 发布

推送到 main 后自动构建发布 site/。现有仓库也启用了根目录发布，镜像内容使两种发布源保持一致。推荐在 Settings → Pages 最终只保留 GitHub Actions。

## 简历与媒体

cv.html 可阅读并通过浏览器打印保存 PDF，不含电话或学号。不是原始求职 PDF 的上传副本。目前没有真实项目照片或视频；系统链路描述不是演示结果。RAPID 资料未完整确认，暂不展示。

## 表述规则

复现与上游贡献明确区分。约 303 N 是特定条件下的仿真峰值，不代表真机或平均成绩。未经发表的研究不能列为正式发表。不要上传原始经历库、密钥、会话快照或未经脱敏的附件。
