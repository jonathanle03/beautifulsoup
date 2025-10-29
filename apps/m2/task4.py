from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
from bs4.filter import SoupStrainer
import warnings
import sys

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

if len(sys.argv) != 2:
  raise Exception("Invalid usage: python task4.py <filename>")

soup = None
strainer = SoupStrainer(id=True)
try:
  with open(sys.argv[1], "r") as fp:
    soup = BeautifulSoup(fp, "lxml", parse_only=strainer)
except Exception:
  try:
    with open(sys.argv[1], "r") as fp:
      soup = BeautifulSoup(fp, "lxml-xml", parse_only=strainer)
  except Exception:
    print("File is not HTML or XML")
    sys.exit(1)

print(soup.prettify())
