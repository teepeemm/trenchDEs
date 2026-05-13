
import re
from glob import glob

def replace_over(content: str) -> str:
  content = re.sub(r'''{
                    ([ a-zA-Z0-9^_\\+!.'-]+)  # a simple group (no parentheses or grouping)
                    \\over(\s*|(?=\W))''',  # watch out for \overline
                    r'\\frac{\1}{', content, flags=re.VERBOSE)
  # but \left(...\right) forms its own group
  content = re.sub(r'''(?<=\\left[({[|])  # left ({[|
                    ([ a-zA-Z0-9^_\\+!.'-]+)  # a simple group
                    \\over\s*
                    ([ a-zA-Z0-9^_\\+!.'-]+)  # a simple group
                    (?=\\right[)}\]|])''',  # right )}]|
                    r'\\frac{\1}{\2}', content, flags=re.VERBOSE)
  return content

def trim_trailing_space(content: str) -> str:
  content = re.sub(r'(?<=\\item\\label{exer:\d+.\d+.\d+})\s*$', '%', content)
  content = re.sub(r'(?<=\\item\\label{exer:\d+.\d+.\d+})\s+(?=\S)', '', content)
  return content

for texfile in glob('*.tex'):
  with open(texfile) as tex:
    mathopen = False
    content = tex.read()
  content = trim_trailing_space(content)
  with open(texfile,'w') as tex:
    tex.write(content)
