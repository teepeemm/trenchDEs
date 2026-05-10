
import re
from glob import glob

for texfile in glob('*.tex'):
  with open(texfile) as tex:
    mathopen = False
    content = tex.read()
  content = re.sub(r'{(\d+)\\over(\d+)}',r'\\frac{\1}{\2}',content)
  with open(texfile,'w') as tex:
    tex.write(content)
