#!/usr/bin/env python3
from html import unescape
from pathlib import Path
from textwrap import dedent
import re
import subprocess

REPO = Path(__file__).resolve().parent.parent
SOURCE_MD = Path('/home/d00d/2026-reflection.md')
ASSETS_DIR = REPO / 'assets'
CSS_URL = 'https://gprocunier.github.io/calabi/assets/site.css'


def run(*args: str) -> str:
    return subprocess.check_output(args, text=True)


def build_readme(source_md: str) -> str:
    header = dedent(
        '''
        # Deterministic Density

        **A practical reflection on deterministic virtualization, cgroup tiering, and why symmetric Gold/Silver/Bronze capacity changes the density conversation.**

        [![License: GPL-3.0](https://img.shields.io/github/license/gprocunier/deterministic-density)](LICENSE)
        ![AMD EPYC 9005](https://img.shields.io/badge/AMD-EPYC%209005-black)
        ![Cgroup Tiering](https://img.shields.io/badge/Cgroup-Tiering-red)
        ![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue)

        <a href="https://gprocunier.github.io/deterministic-density/"><kbd>&nbsp;&nbsp;OPEN THE ESSAY&nbsp;&nbsp;</kbd></a>
        <a href="https://github.com/gprocunier/openstack-cgroup-tiering"><kbd>&nbsp;&nbsp;CGROUP THESIS&nbsp;&nbsp;</kbd></a>
        <a href="https://gprocunier.github.io/calabi/host-resource-management.html"><kbd>&nbsp;&nbsp;CALABI PROJECT&nbsp;&nbsp;</kbd></a>

        ## Site Build

        Regenerate the repo `README.md`, root `index.html`, and copied `assets/site.css` with:

        ```bash
        ./scripts/build_site.py
        ```

        ---

        '''
    )
    return header + source_md


def build_css() -> str:
    css = run('bash', '-lc', f'curl -L --silent {CSS_URL}')
    css += dedent(
        '''

        .note {
          margin: 1.25rem 0;
          padding: 0.85rem 1rem;
          background: var(--rh-gray-10);
          border-left: 0.35rem solid var(--rh-link);
        }

        .note .title p {
          margin: 0 0 0.4rem;
          font-weight: 700;
        }
        '''
    )
    return css


def render_article() -> str:
    html = run('pandoc', '-f', 'gfm', '-t', 'html5', str(SOURCE_MD))
    pattern = re.compile(r'<pre class="mermaid"><code>(.*?)</code></pre>', re.S)
    return pattern.sub(lambda m: '<div class="mermaid">' + unescape(m.group(1)) + '</div>', html)


def build_index(article_html: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Deterministic Density</title>
    <meta name="description" content="A practical reflection on deterministic virtualization, cgroup tiering, and why symmetric Gold, Silver, and Bronze capacity changes the density conversation.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@500;700&family=Red+Hat+Mono:wght@400;500&family=Red+Hat+Text:wght@400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/site.css">
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
      mermaid.initialize({{
        startOnLoad: true,
        theme: 'base',
        securityLevel: 'loose',
        flowchart: {{
          useMaxWidth: true,
          htmlLabels: true,
          nodeSpacing: 30,
          rankSpacing: 42
        }},
        themeVariables: {{
          fontFamily: '"Red Hat Text", "Helvetica Neue", Arial, sans-serif',
          fontSize: '18px',
          primaryColor: '#fff4e5',
          primaryBorderColor: '#e0e0e0',
          primaryTextColor: '#151515',
          lineColor: '#8a8d90',
          clusterBkg: '#ffffff',
          clusterBorder: '#c7c7c7'
        }}
      }});
    </script>
  </head>
  <body>
    <div class="site-shell">
      <header class="site-header">
        <div class="site-header__inner">
          <p class="eyebrow">Deterministic Density</p>
          <div class="site-brand">
            <div>
              <h1 class="site-brand__title"><a href="index.html">Deterministic Density</a></h1>
              <p class="site-brand__tagline">A practitioner’s editorial on cgroup tiering, Effective Constrained Clock, and why symmetric CPU tiers change the economics of virtualization density.</p>
            </div>
          </div>
          <div class="site-header__actions">
            <a href="https://github.com/gprocunier/deterministic-density"><kbd>READ ON GITHUB</kbd></a>
            <a href="https://github.com/gprocunier/openstack-cgroup-tiering"><kbd>CGROUP THESIS</kbd></a>
            <a href="https://gprocunier.github.io/calabi/host-resource-management.html"><kbd>CALABI PROJECT</kbd></a>
          </div>
        </div>
      </header>
      <main class="page-shell">
        <div class="content-column">
          <article class="markdown-body">
            <p><a href="https://github.com/gprocunier/deterministic-density/blob/main/LICENSE"><img alt="License: GPL-3.0" src="https://img.shields.io/github/license/gprocunier/deterministic-density"></a>
            <img alt="AMD EPYC 9005" src="https://img.shields.io/badge/AMD-EPYC%209005-black">
            <img alt="Cgroup Tiering" src="https://img.shields.io/badge/Cgroup-Tiering-red">
            <img alt="GitHub Pages" src="https://img.shields.io/badge/GitHub-Pages-blue"></p>
            {article_html}
          </article>
        </div>
        <aside class="side-column">
          <section class="context-block">
            <h2>Why This Matters</h2>
            <p>The practical claim here is simple: symmetric tiering turns wasted flat-pool headroom into usable mixed-tenancy capacity without giving up a clear contention model.</p>
          </section>
          <section class="source-block">
            <h2>Primary Links</h2>
            <ul class="path-list">
              <li>
                <a href="https://github.com/gprocunier/deterministic-density">
                  <strong>Repository</strong>
                  <span>Source for this essay and Pages site.</span>
                </a>
              </li>
              <li>
                <a href="https://github.com/gprocunier/openstack-cgroup-tiering">
                  <strong>2025 Cgroup Thesis</strong>
                  <span>The original OpenStack cgroup-tiering work.</span>
                </a>
              </li>
              <li>
                <a href="https://gprocunier.github.io/calabi/host-resource-management.html">
                  <strong>Calabi Project</strong>
                  <span>The single-host KVM and OpenShift adaptation.</span>
                </a>
              </li>
            </ul>
          </section>
          <section class="toc-block">
            <h2>On This Page</h2>
            <ul>
              <li><a href="#deterministic-virtualization-rethinking-cpu-architecture-with-cgroup-tiering">Overview</a></li>
              <li><a href="#1-the-density-paradigm-traditional-virtualization-vs-guardrail-tiering">The Density Paradigm</a></li>
              <li><a href="#2-the-foundation-strict-isolation-and-symmetric-tiering">Strict Isolation and Symmetric Tiering</a></li>
              <li><a href="#3-effective-constrained-clock-ecc-and-the-sla-floor">ECC and the SLA Floor</a></li>
              <li><a href="#4-map-latency-tolerance-not-environments">Map Latency Tolerance</a></li>
              <li><a href="#5-the-sweet-spot-and-idle-borrowing">Idle Borrowing</a></li>
              <li><a href="#6-capacity-planning-traditional-vs-tiered-density">Capacity Planning</a></li>
              <li><a href="#scenario-a-t-shirt-sizing-optimal-density-stacking">Scenario A</a></li>
              <li><a href="#scenario-b-openshift-estate-and-orthogonal-tenancy">Scenario B</a></li>
              <li><a href="#conclusion-density-vs-baseline-sla-guarantees">Conclusion</a></li>
            </ul>
          </section>
        </aside>
      </main>
      <footer class="site-footer">
        Published from repository docs on 2026-04-12.
      </footer>
    </div>
  </body>
</html>
'''


def main() -> None:
    source_md = SOURCE_MD.read_text()
    ASSETS_DIR.mkdir(exist_ok=True)
    (REPO / '.nojekyll').write_text('')
    (REPO / 'README.md').write_text(build_readme(source_md))
    (ASSETS_DIR / 'site.css').write_text(build_css())
    (REPO / 'index.html').write_text(build_index(render_article()))


if __name__ == '__main__':
    main()
