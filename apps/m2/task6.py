import sys
import warnings
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from bs4.filter import SoupReplacer

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

if len(sys.argv) != 2:
  raise Exception("Invalid usage: python task5.py <filename>")

soup = None
replacer = SoupReplacer("b", "blockquote")
try:
  with open(sys.argv[1], "r") as fp:
    soup = BeautifulSoup(fp, "lxml", replacer=replacer)
except Exception:
  try:
    with open(sys.argv[1], "r") as fp:
      soup = BeautifulSoup(fp, "lxml-xml", replacer=replacer)
  except Exception:
    print("File is not HTML or XML")
    sys.exit(1)


with open("pretty_file.txt", "w") as fp:
  fp.write(soup.prettify())