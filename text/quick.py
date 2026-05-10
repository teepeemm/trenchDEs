
from glob import glob

for texfile in glob('*.tex'):
  with open(texfile) as tex:
    mathopen = False
    content = tex.read()
  while '$$' in content:
    if mathopen:
      content = content.replace('$$',r'\]',1)
    else:
      content = content.replace('$$',r'\[',1)
    mathopen = not mathopen
  with open(texfile,'w') as tex:
    tex.write(content)
