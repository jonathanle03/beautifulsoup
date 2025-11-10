import pytest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer
from . import SoupTest

class TestSoupReplacer(SoupTest):
    def test_name_tags_doc_ex(self):
        html_doc = """
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.
        </p>
        """

        replacer = SoupReplacer(og_tag="b", alt_tag="blockquote")
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
    
    def test_name_tags_nested(self):
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

        replacer = SoupReplacer(og_tag="ul", alt_tag="ol")
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

    def test_name_xformer_doc_ex(self):
        html_doc = """
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.
        </p>
        """

        name_xformer = lambda name: "blockquote" if name == "b" else name
        replacer = SoupReplacer(name_xformer=name_xformer)
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
    
    def test_name_xformer_nested(self):
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

        name_xformer = lambda name: "ol" if name == "ul" else name
        replacer = SoupReplacer(name_xformer=name_xformer)
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
    
    def test_attrs_xformer_doc_ex(self):
        html_doc = """
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.
        </p>
        """

        attrs_xformer = lambda attrs: {key: value for key, value in attrs.items() if key != "class"}
        replacer = SoupReplacer(attrs_xformer=attrs_xformer)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

        expected = \
"""
<p>
 <b>
  The Dormouse's story
 </b>
</p>
<p>
 Once upon a time there were three little sisters; and their names were
 <a href="http://example.com/elsie" id="link1">
  Elsie
 </a>
 ,
 <a href="http://example.com/lacie" id="link2">
  Lacie
 </a>
 and
 <a href="http://example.com/tillie" id="link3">
  Tillie
 </a>
 ; and they lived at the bottom of a well.
</p>
"""

        assert soup.prettify().strip() == expected.strip()
    
    def test_attrs_xformer_nested(self):
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

        attrs_xformer = lambda attrs: attrs if "href" not in attrs else attrs | {"href": "https://www.google.com"}
        replacer = SoupReplacer(attrs_xformer=attrs_xformer)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

        expected = \
"""
<nav>
 <ul>
  <li>
   <a href="https://www.google.com">
    Intro
   </a>
  </li>
  <li>
   <a href="https://www.google.com">
    Work
   </a>
  </li>
  <li>
   <a href="https://www.google.com">
    About
   </a>
  </li>
  <li>
   <a href="https://www.google.com">
    Contact
   </a>
  </li>
 </ul>
</nav>
"""

        assert soup.prettify().strip() == expected.strip()
    
    def test_name_xformer_nested(self):
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

        name_xformer = lambda name: "ol" if name == "ul" else name
        replacer = SoupReplacer(name_xformer=name_xformer)
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
    
    def test_xformer_doc_ex(self):
        html_doc = """
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.
        </p>
        """

        def xformer(tag):
            if "class" in tag.attrs:
                del tag.attrs["class"]
        replacer = SoupReplacer(xformer=xformer)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

        expected = \
"""
<p>
 <b>
  The Dormouse's story
 </b>
</p>
<p>
 Once upon a time there were three little sisters; and their names were
 <a href="http://example.com/elsie" id="link1">
  Elsie
 </a>
 ,
 <a href="http://example.com/lacie" id="link2">
  Lacie
 </a>
 and
 <a href="http://example.com/tillie" id="link3">
  Tillie
 </a>
 ; and they lived at the bottom of a well.
</p>
"""

        assert soup.prettify().strip() == expected.strip()
    
    def test_xformer_nested(self):
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

        def xformer(tag):
            if "href" in tag.attrs:
                tag.attrs["href"] = "https://www.google.com"
        replacer = SoupReplacer(xformer=xformer)
        soup = BeautifulSoup(html_doc, "html.parser", replacer=replacer)

        expected = \
"""
<nav>
 <ul>
  <li>
   <a href="https://www.google.com">
    Intro
   </a>
  </li>
  <li>
   <a href="https://www.google.com">
    Work
   </a>
  </li>
  <li>
   <a href="https://www.google.com">
    About
   </a>
  </li>
  <li>
   <a href="https://www.google.com">
    Contact
   </a>
  </li>
 </ul>
</nav>
"""

        assert soup.prettify().strip() == expected.strip()