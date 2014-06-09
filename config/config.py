#!/usr/bin/python3
{
    # main.tex options
    'extra_packages': [
        ('longtable', ''),
        ('custom', ''),
        ],
    # style.sty options
    'bibliography_resources': [
        '../content/bibliography.bib',
        ],
    # other options
    'git': [
        ('dump_log', {
            'output': 'git_log.tex',
            'format': 'format:%H&&\\\\\n%an & %ai & %s \\\\\n\\hline\n',
            'path': '../content',
            }),
        ],
    'template_files': [
        # original
        'main.tex',
        'pre-text.tex',
        'post-text.tex',
        'chapters.tex',
        'documentation.cls',
        'lithuanian.lbx',
        'title.sty',
        'global-config.tex',
        'bibliography.bib',
        'pglossary.py',
        'pglossary.sty',
        # new
        'custom.sty',
        ],
    }
