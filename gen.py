import xml.etree.ElementTree as ET
from itertools import zip_longest

# from IPython import embed; embed()
# ET.register_namespace('', "http://www.topografix.com/GPX/1/1")
ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
ET.register_namespace("cc", "http://creativecommons.org/ns#")
ET.register_namespace("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
ET.register_namespace("svg", "http://www.w3.org/2000/svg")
ET.register_namespace("", "http://www.w3.org/2000/svg")
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
ET.register_namespace("sodipodi", "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd")
ET.register_namespace("inkscape", "http://www.inkscape.org/namespaces/inkscape")


lines = open("orgs.csv").readlines()
names = [line.strip() for line in lines]

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def split_name(name):
  if not name or not name.strip():
    return " ", " "
  parts = name.split()
  jmeno = " ".join(parts[:-1])
  if jmeno.strip() == "":
    return name, ""
  prijmeni = parts[-1]
  return jmeno, prijmeni

for i, (n1, n2, n3, n4) in enumerate(grouper(names, 4)):
  tree = ET.parse('orgs.svg')
  root = tree.getroot()

  # from IPython import embed; embed()
  # sys.exit()
  elems = list(root.iter("{http://www.w3.org/2000/svg}flowPara"))
  
  jmena = [e for e in elems if e.text == "AAA"]
  prijmeni = [e for e in elems if e.text == "BBB"]


  name, surname = split_name(n1)
  jmena[0].text = name
  prijmeni[0].text = surname

  name, surname = split_name(n2)
  jmena[1].text = name
  prijmeni[1].text = surname

  name, surname = split_name(n3)
  jmena[2].text = name
  prijmeni[2].text = surname

  name, surname = split_name(n4)
  jmena[3].text = name
  prijmeni[3].text = surname

  tree.write(open("{}a.svg".format(i), 'w'), encoding='unicode')

  name, surname = split_name(n1)
  jmena[1].text = name
  prijmeni[1].text = surname

  name, surname = split_name(n2)
  jmena[0].text = name
  prijmeni[0].text = surname

  name, surname = split_name(n3)
  jmena[3].text = name
  prijmeni[3].text = surname

  name, surname = split_name(n4)
  jmena[2].text = name
  prijmeni[2].text = surname

  tree.write(open("{}b.svg".format(i), 'w'), encoding='unicode')

# for neighbor in root.iter("{http://www.w3.org/2000/svg}tspan"):
  # print (neighbor.text="CCC DDD")