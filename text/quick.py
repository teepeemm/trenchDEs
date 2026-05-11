
import re
from glob import glob

for texfile in glob('*.tex'):
  with open(texfile) as tex:
    mathopen = False
    content = tex.read()
  content = re.sub(r'{([a-zA-Z0-9^_\\]+)\\over\s*(?=\W)',r'\\frac{\1}{',content)
#  content = re.sub(r'{(\d+)\\over\s*(\d+)}',r'\\frac{\1}{\2}',content)
  with open(texfile,'w') as tex:
    tex.write(content)
