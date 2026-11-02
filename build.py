"""Build a dependency-free static portfolio. Python 3.9+."""
import json
from html import escape
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'site'
C = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
def e(value):
    return escape(str(value), quote=True)
def link(url, label, local=False):
    if not url:
        return '<span class="pending">' + e(label) + ' · coming soon</span>'
    if local:
        target = (OUT / url).resolve()
        if not target.is_relative_to(OUT.resolve()) or not target.is_file() or target.suffix.lower() != '.pdf':
            raise ValueError('PDF must exist inside site/: ' + url)
    elif urlparse(url).scheme != 'https' or not urlparse(url).netloc:
        raise ValueError('Use a full HTTPS URL: ' + url)
    return '<a class="text-link" href="' + e(url) + '">' + e(label) + ' ↗</a>'

NAV = [('index.html','Home'),('research.html','Research'),('projects.html','Projects'),('cv.html','CV / Resume'),('about.html','About / Contact')]
def page(file, title, body):
    nav = ''.join('<a '+('aria-current="page" ' if file == f else '')+'href="'+f+'">'+t+'</a>' for f,t in NAV)
    draft = '<div class="draft">PREVIEW · Content awaits owner review. No publication or performance claims are verified.</div>' if not C['reviewed_for_publication'] else ''
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{e(C['name'])}: embodied intelligence, robotics, research and engineering portfolio.">
{'' if C['reviewed_for_publication'] else '<meta name="robots" content="noindex,nofollow">'}
<title>{e(title)} · {e(C['name'])}</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="assets/style.css"></head>
<body><a class="skip" href="#main">Skip to content</a>{draft}<header><a class="brand" href="index.html"><span class="brand-mark">↗</span> {e(C['name'])}</a><nav aria-label="Main navigation">{nav}</nav></header>
<main id="main">{body}</main><footer><span>{e(C['name'])} · Research & engineering</span><span>Built with curiosity. Backed by evidence.</span><a href="about.html">Get in touch ↗</a></footer></body></html>'''
    (OUT / file).write_text(html, encoding='utf-8')

def cases(items):
    return ''.join(f'''<article class="case"><div class="case-top"><span class="eyebrow">CASE {i:02}</span><span class="tag">{e(p['status'])}</span></div><h2>{e(p['title'])}</h2><dl><dt>Background</dt><dd>{e(p['background'])}</dd><dt>My contribution</dt><dd>{e(p['contribution'])}</dd><dt>Technical stack</dt><dd>{e(p['stack'])}</dd><dt>Evidence & results</dt><dd>{e(p['result'])}</dd></dl>{link(p['url'],'Project evidence')}</article>''' for i,p in enumerate(items,1))

OUT.mkdir(exist_ok=True)
page('index.html','Home',f'''
<section class="hero"><div><p class="eyebrow">ROBOTICS / EMBODIED INTELLIGENCE</p><h1>From ideas<br>to systems<br><em>that act.</em></h1><p class="intro">{e(C['intro'])}</p><p class="affiliation">{e(C['affiliation'])}</p><div class="buttons"><a class="button" href="research.html">Explore research <span>↗</span></a><a class="button secondary" href="projects.html">Explore projects <span>↗</span></a></div></div>
<figure class="diagram"><div class="diagram-label"><span>PERCEPTION → ACTION</span><span>01 / SYSTEM VIEW</span></div><svg viewBox="0 0 440 400" role="img" aria-labelledby="diagram-title"><title id="diagram-title">Conceptual robot perception and action loop; an illustration, not an experimental result</title><defs><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#b8c7c2"/></pattern></defs><rect width="440" height="400" fill="url(#grid)"/><ellipse cx="224" cy="310" rx="155" ry="42" fill="none" stroke="#9eafa9"/><path d="M70 310h308M224 270v80" stroke="#bbc8c1"/><path d="M194 301v-25l30-16 30 16v25l-30 16z" fill="#182f36"/><path d="M224 275l-25-64 57-77" fill="none" stroke="#182f36" stroke-width="23" stroke-linejoin="round"/><path d="M256 134l56 33" stroke="#d26b3d" stroke-width="18"/><path d="M311 164l16-17m-16 17l-4 23" stroke="#182f36" stroke-width="8"/><circle cx="199" cy="211" r="13" fill="#f7f5ed" stroke="#182f36" stroke-width="5"/><circle cx="256" cy="134" r="12" fill="#f7f5ed" stroke="#182f36" stroke-width="5"/><path d="M80 135l57-31 31 18-57 32z" fill="#d26b3d" opacity=".8"/><path d="M80 135v43l31 19v-43m0 43l57-32v-43" fill="none" stroke="#d26b3d" stroke-width="2"/><path d="M138 205q-25 40 5 60M301 245q44-38 32-64" fill="none" stroke="#7f9489" stroke-dasharray="5 5"/><text x="56" y="82" font-family="monospace" font-size="11" fill="#49625a">OBSERVE</text><text x="306" y="229" font-family="monospace" font-size="11" fill="#49625a">ACT</text></svg><figcaption>A conceptual loop: observe, reason, act, evaluate.</figcaption></figure></section>
<section class="paths"><div><p class="eyebrow">TWO WAYS IN</p><h2>Research questions.<br>Engineering decisions.</h2></div><a class="path" href="research.html"><span class="eyebrow">FOR RESEARCH GROUPS</span><h3>How I investigate <span>↗</span></h3><p>Research interests, reproduction notes, and evidence of experimental work.</p></a><a class="path" href="projects.html"><span class="eyebrow">FOR ENGINEERING TEAMS</span><h3>How I build <span>↗</span></h3><p>Project context, personal contributions, technical choices, and verifiable outcomes.</p></a></section>
<section class="selected"><div><p class="eyebrow">CURRENT FOCUS</p><h2>Build. Measure. Investigate.</h2><p>My current portfolio connects humanoid motion tracking, dexterous-hand teleoperation, and perception-to-control engineering. I distinguish upstream algorithms from my integration and evaluation work.</p></div><a class="text-link" href="research.html">View research notes ↗</a></section>''')
page('research.html','Research','''<section class="page-heading"><p class="eyebrow">01 / RESEARCH</p><h1>Questions into<br><em>experiments.</em></h1><p>Interests in embodied intelligence and robotics, developed through reproduction and careful evaluation.</p></section>'''+cases(C['research'])+'''<aside class="note"><h3>Publication status</h3><p>No peer-reviewed publication is claimed here. Reproductions, work in progress, preprints, and accepted papers must be labeled separately, with original sources and accurate authorship.</p></aside>''')
page('projects.html','Projects','''<section class="page-heading"><p class="eyebrow">02 / PROJECTS</p><h1>Make it work.<br><em>Show the evidence.</em></h1><p>Engineering case studies organized around the problem, my contribution, and what can be verified.</p></section>'''+cases(C['projects']))
page('cv.html','CV / Resume',f'''<section class="page-heading"><p class="eyebrow">03 / EXPERIENCE</p><h1>One background.<br><em>Two perspectives.</em></h1><p>Choose the document that matches your context.</p></section><section class="experience"><p class="eyebrow">EDUCATION & TECHNICAL PRACTICE</p><h2>Beijing University of Posts and Telecommunications</h2><p>Undergraduate, entering class of 2025 · Computer Science (Yuan program), following a transfer in October 2026. Chinese name: 许庭彰.</p><p>Project experience: humanoid motion tracking, robotic-hand teleoperation, mobile-robot perception and control, and Python automation. See the linked case studies for individual contributions and their limits.</p><p>Tools used across projects: Python, MuJoCo, PPO training tooling, OpenCV, MediaPipe, TCP sockets, serial communication, and Playwright.</p></section><div class="document-grid"><article class="case"><p class="eyebrow">ACADEMIC</p><h2>Curriculum vitae</h2><p>Education, research experience, experimental contributions, and accurately labeled scholarly work.</p>{link(C['cv_pdf'],'Academic CV (PDF)',True)}</article><article class="case"><p class="eyebrow">INDUSTRY</p><h2>Technical resume</h2><p>A concise account of engineering projects, individual responsibilities, and supported outcomes.</p>{link(C['resume_pdf'],'Technical resume (PDF)',True)}</article></div><aside class="note">Documents have not been supplied yet. Downloads become available only after real PDFs are added.</aside>''')
email = C['email']
if email and (any(x in email for x in '\r\n ?&#') or '@' not in email):
    raise ValueError('Invalid email')
contact = f'<a class="text-link" href="mailto:{e(email)}">{e(email)} ↗</a>' if email else '<span class="pending">Contact email · to be added</span>'
page('about.html','About / Contact',f'''<section class="page-heading"><p class="eyebrow">04 / ABOUT</p><h1>Curious about<br><em>intelligent machines.</em></h1><p>{e(C['affiliation'])}</p></section><section class="about-grid"><div><p class="eyebrow">许庭彰 / TINGZHANG XU</p><h2>About me</h2><p>{e(C['intro'])}</p><p>This portfolio brings research reproduction and engineering work together. My experience spans humanoid simulation, robotic-hand hardware integration, mobile-robot control, and software tooling. I am interested in research opportunities and technical internships in robotics and AI systems.</p><h2>What I want to explore</h2><p>Embodied intelligence, robotics, and the relationship between experimental ideas and working systems.</p></div><aside class="contact"><p class="eyebrow">LET’S CONNECT</p><h2>Start a conversation.</h2><p>For research opportunities and technical roles.</p>{contact}<br>{link(C['github'],'GitHub')}</aside></section>''')
(OUT / '.nojekyll').touch()
print('Built 5 pages in ' + str(OUT))
