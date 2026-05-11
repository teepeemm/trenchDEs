
import re
from glob import glob

for texfile in glob('*.tex'):
  with open(texfile) as tex:
    mathopen = False
    content = tex.read()
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
  with open(texfile,'w') as tex:
    tex.write(content)
