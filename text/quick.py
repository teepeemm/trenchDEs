
import re
from glob import glob

def replace_over(content: str) -> str:
  content = re.sub(r'''{
                    ([ a-zA-Z0-9^_\\+!.'-]+)  # a simple group (no parentheses or grouping)
                    \\over(\s+|(?=\W))''',  # watch out for \overline
                    r'\\frac{\1}{', content, flags=re.VERBOSE)
  # but \left(...\right) forms its own group
  content = re.sub(r'''(?<=\\left[({[|])  # left ({[|
                    ([ a-zA-Z0-9^_\\+!.'-]+)  # a simple group
                    \\over(\s+|(?=\W))
                    ([ a-zA-Z0-9^_\\+!.'-]+)  # a simple group
                    (?=\\right[)}\]|])''',  # right )}]|
                    r'\\frac{\1}{\2}', content, flags=re.VERBOSE)
  return content

def use_eqref(content: str) -> str:
  content = re.sub(r'\(\\(ref{eq:\d+\.\d+\.\d+})\)', r'\\eq\1', content)
  return content

def trim_trailing_space(content: str) -> str:
  content = re.sub(r'(?<=\\item\\label{exer:)(\d+.\d+.\d+})\s*$', r'\1%', content)
  content = re.sub(r'(?<=\\item\\label{exer:)(\d+.\d+.\d+})\s+(?=\S)', r'\1', content)
  return content

def change_graphics_height(content: str) -> str:
  content = content.replace('height=3.66in', 'height=3.3in')
  return content

def respace(content: str) -> str:
  content = content.replace(r'\mbox{\quad and ?\quad}', r'\quad\text{and}\quad ')
  return content

def addtag(content: str) -> str:
  content = re.sub(r'\\eqno\{\\rm ?\((\w)\)\}', r'\\tag{\1}', content)
  return content

for texfile in glob('*.tex'):
  with open(texfile) as tex:
    mathopen = False
    content = tex.read()
  content = respace(content)
  with open(texfile,'w') as tex:
    tex.write(content)

'''
mbox, ref, eqnarray, cases, part, solutionpart, scalebox, noindent, dst, jot, eqno, over
bf, it, rm
Section, Chapter, Figure, Table, Exercise, Example, Equation, Eqn, Theorem
TODO
units
tabular, array, enlargethispage, $,$, $.$
'''
