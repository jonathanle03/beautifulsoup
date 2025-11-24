from bs4 import BeautifulSoup
from bs4 import XMLParsedAsHTMLWarning
from bs4.filter import SoupStrainer
import warnings
import sys

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

if len(sys.argv) != 2:
  raise Exception("Invalid usage: python task2.py <filename>")

soup = None
try:
  with open(sys.argv[1], "r") as fp:
    soup = BeautifulSoup(fp, "lxml")
except Exception:
  try:
    with open(sys.argv[1], "r") as fp:
      soup = BeautifulSoup(fp, "lxml-xml")
  except Exception:
    print("File is not HTML or XML")
    sys.exit(1)

for node in soup:
  if node.name == "a":
    print(node)
