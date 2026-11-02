"""Build Chinese recruiting pages and retain the English research portfolio."""
import json
import shutil
import subprocess
import sys
import re
from pathlib import Path
from html import escape as e

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'site'
C = json.loads((ROOT/'content.json').read_text(encoding='utf-8'))
P = json.loads((ROOT/'content-zh.json').read_text(encoding='utf-8'))
NAV = [('index.html','首页'),('projects.html','项目'),('research.html','科研'),('cv.html','简历'),('about.html','联系')]
EMAIL=e(C['email'])
def page(file,title,body):
    nav=''.join(f'<a href="{f}"'+(' aria-current="page"' if file==f else '')+f'>{t}</a>' for f,t in NAV)
    html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · 许庭彰</title><meta name="description" content="许庭彰，北邮计算机类本科生。机器人学习、灵巧手遥操作与 Python 工程项目。"><link rel="stylesheet" href="assets/style.css"><link rel="stylesheet" href="assets/recruit.css"><link rel="icon" href="assets/favicon.svg"></head><body class="recruit"><a class="skip" href="#main">跳到正文</a><header><a class="brand" href="index.html">许庭彰 <small>Tingzhang Xu</small></a><nav aria-label="主导航">{nav}<a href="en/index.html" lang="en">EN ↗</a></nav></header><main id="main">{body}</main><footer><span>许庭彰 · 北京邮电大学</span><span>机器人学习 / 工程系统</span><a href="mailto:{EMAIL}">邮件联系 ↗</a></footer></body></html>'''
    (OUT/file).write_text(html,encoding='utf-8')
def flow(p):
    return '<div class="pipeline" aria-label="系统链路">'+''.join('<span>'+e(x)+'</span>' for x in p['flow'])+'</div>'
def repo(p):
    return f'<a class="text-link" href="{e(p["url"])}">查看代码与技术记录 ↗</a>' if p['url'] else ''
def cards():
    return ''.join(f'''<article class="project-card"><div class="card-top"><span class="eyebrow">0{i+1} / {e(p['scope'])}</span><a href="projects.html#{p['id']}" aria-label="查看{e(p['subtitle'])}详情">↗</a></div><h3><a href="projects.html#{p['id']}">{e(p['title'])}</a></h3><p class="subtitle">{e(p['subtitle'])}</p>{flow(p)}<p>{e(p['short'])}</p><div class="evidence">{e(p['evidence'])}</div><p class="stack">{e(p['stack'])}</p><div class="card-links"><a href="projects.html#{p['id']}">我的贡献与结果 →</a><a href="{e(p['url'])}">GitHub ↗</a></div></article>''' for i,p in enumerate(P[:3]))
def cases(items):
    return ''.join(f'''<article class="case" id="{p['id']}"><div class="case-top"><span class="eyebrow">{e(p['subtitle'])}</span><span class="tag">{e(p['scope'])}</span></div><h2>{e(p['title'])}</h2><p class="role">我的角色：{e(p['role'])}</p>{flow(p)}<dl><dt>要解决的问题</dt><dd>{e(p['problem'])}</dd><dt>我做了什么</dt><dd>{e(p['contribution'])}</dd><dt>结果与证据</dt><dd>{e(p['result'])}</dd><dt>技术栈</dt><dd>{e(p['stack'])}</dd></dl><details><summary>实验范围与贡献边界</summary><p>{e(p['boundary'])}</p></details>{repo(p)}</article>''' for p in items)

OUT.mkdir(exist_ok=True)
page('index.html','首页',f'''<section class="recruit-hero"><div><p class="eyebrow">机器人学习 · 实机集成 · PYTHON 工程</p><h1>许庭彰<span>Tingzhang Xu</span></h1><p class="identity">北京邮电大学 · 计算机类（元班）· 大二</p><p class="lead">从机器人动作训练，到视觉与硬件闭环。<br>我关注算法如何在具体系统中运行、调试和验证。</p><div class="buttons"><a class="button" href="cv.html">查看简历 <span>↗</span></a><a class="button secondary" href="projects.html">浏览项目 <span>↓</span></a></div></div><aside class="profile-summary"><span class="eyebrow">机会方向</span><h2>机器人 / AI 工程实习<br>具身智能科研机会</h2><dl><dt>已有实践</dt><dd>G1 运动跟踪、灵巧手遥操作、视觉控制、Python 自动化</dd><dt>项目证据</dt><dd>三个公开仓库，附实现与技术记录</dd><dt>联系</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></dl><a class="text-link" href="{e(C['github'])}">GitHub / yantingweb ↗</a></aside></section><section class="featured"><div class="section-title"><div><p class="eyebrow">SELECTED WORK</p><h2>先看这三个项目</h2></div><a class="text-link" href="projects.html">全部项目 →</a></div><div class="project-grid">{cards()}</div></section><section class="audience"><div><p class="eyebrow">技术岗位</p><h2>看系统实现与排错能力</h2><p>环境适配、协议调试、模块设计，以及从问题定位到验证的过程。</p><a class="text-link" href="cv.html">查看求职简历 →</a></div><div><p class="eyebrow">科研申请</p><h2>看复现与实验判断</h2><p>动作跟踪、重定向复现与评估可靠性；明确区分上游算法和个人贡献。</p><a class="text-link" href="research.html">查看科研实践 →</a></div></section>''')
page('projects.html','项目','''<section class="page-heading"><p class="eyebrow">PROJECTS / 工程实践</p><h1>做了什么，<br>如何验证。</h1><p>按问题、个人贡献和证据展开，代码与技术文档可直接查看。</p></section>'''+cases(P))
page('research.html','科研','''<section class="page-heading"><p class="eyebrow">RESEARCH / 科研实践</p><h1>机器人学习，<br>从复现与验证开始。</h1><p>关注运动跟踪、视觉重定向，以及仿真评估与实机系统之间的差异。以下是研究导向的工程实践，非正式发表论文。</p></section>'''+cases([P[1],P[0]]))
resume_projects=''.join(f'''<article class="resume-project"><h3>{e(p['subtitle'])}</h3><p><strong>个人贡献：</strong>{e(p['contribution'])}</p><p><strong>结果：</strong>{e(p['result'])}</p>{repo(p)}</article>''' for p in P[:3])
page('cv.html','简历',f'''<section class="resume-header"><div><p class="eyebrow">RESUME / 求职简历</p><h1>许庭彰 <span>Tingzhang Xu</span></h1><p>机器人 / AI 工程实习 · 具身智能科研机会</p><p><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{e(C['github'])}">github.com/yantingweb</a></p></div><button class="button" type="button" id="print-resume">打印 / 保存 PDF ↗</button></section><section class="resume-section"><h2>教育背景</h2><p><strong>北京邮电大学 · 未来学院 · 计算机类（元班）</strong></p><p>2025 级本科生，现大二；2026 年 10 月由低空技术与工程转入计算机类。</p></section><section class="resume-section"><h2>技术实践</h2><p><strong>机器人与视觉：</strong>MuJoCo、PPO 训练工具链、OpenCV、MediaPipe、DexPilot 使用与标定。</p><p><strong>工程与工具：</strong>Python、TCP Socket、串口通信、树莓派、Playwright、命令行与定时任务。</p></section><section class="resume-section"><h2>代表项目</h2>{resume_projects}</section><script src="assets/print.js" defer></script>''')
page('about.html','联系',f'''<section class="page-heading"><p class="eyebrow">ABOUT / CONTACT</p><h1>许庭彰</h1><p>北邮计算机类本科生，关注机器人学习与工程系统。</p></section><section class="about-grid"><div><h2>从具体问题开始</h2><p>我在 G1 动作训练、灵巧手遥操作、树莓派视觉小车和 Python 工具项目中，积累了环境适配、通信排错、系统集成与实验验证经验。</p><p>希望继续参与机器人、具身智能与 AI 系统方向的研究或工程工作，在实际问题中加深算法和计算机系统基础。</p><a class="text-link" href="cv.html">查看简历 →</a></div><aside class="contact"><p class="eyebrow">联系我</p><h2>科研合作 / 技术实习</h2><a class="text-link" href="mailto:{EMAIL}">{EMAIL}</a><br><a class="text-link" href="{e(C['github'])}">GitHub / yantingweb ↗</a></aside></section>''')
(OUT/'assets'/'print.js').write_text("document.getElementById('print-resume').addEventListener('click', () => window.print());\n",encoding='utf-8')
subprocess.run([sys.executable,str(ROOT/'build_en.py')],check=True)
# English mirrors use the same up-to-date Chinese resume instead of dead PDF links.
en_cv=OUT/'en'/'cv.html'
s=en_cv.read_text(encoding='utf-8')
s=re.sub(r'<div class="document-grid">.*?</aside>', '<p><a class="text-link" href="../cv.html">Read the current Chinese resume / Print to PDF ↗</a></p>', s, flags=re.S)
en_cv.write_text(s,encoding='utf-8')
for p in OUT.glob('*.html'): shutil.copy2(p,ROOT/p.name)
for name in ['assets','en']: shutil.copytree(OUT/name,ROOT/name,dirs_exist_ok=True)
(ROOT/'.nojekyll').touch()
print('Built Chinese recruiting website and English portfolio.')
