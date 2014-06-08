#!/usr/bin/python3
{
    # main.tex options
    'extra_packages': [
        ('longtable', ''),
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
    }
