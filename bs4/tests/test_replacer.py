import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
from . import SoupTest

class TestSoupReplacer(SoupTest):
    def test_documentation_example(self):
        html_doc = """
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.
        </p>
        """

        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

        expected = \
"""
<p class="title">
 <blockquote>
  The Dormouse's story
 </blockquote>
</p>
<p class="story">
 Once upon a time there were three little sisters; and their names were
 <a class="sister" href="http://example.com/elsie" id="link1">
  Elsie
 </a>
 ,
 <a class="sister" href="http://example.com/lacie" id="link2">
  Lacie
 </a>
 and
 <a class="sister" href="http://example.com/tillie" id="link3">
  Tillie
 </a>
 ; and they lived at the bottom of a well.
</p>
"""

        assert soup.prettify().strip() == expected.strip()
    
    def test_nested_doc(self):
        html_doc = """
        <nav>
            <ul>
                <li><a href="#intro">Intro</a></li>
                <li><a href="#work">Work</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
        """

        replacer = SoupReplacer("ul", "ol")
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

        expected = \
"""
<nav>
 <ol>
  <li>
   <a href="#intro">
    Intro
   </a>
  </li>
  <li>
   <a href="#work">
    Work
   </a>
  </li>
  <li>
   <a href="#about">
    About
   </a>
  </li>
  <li>
   <a href="#contact">
    Contact
   </a>
  </li>
 </ol>
</nav>
"""

        assert soup.prettify().strip() == expected.strip()