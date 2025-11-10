# Milestone-3
## SoupReplacer
SoupReplacer is a class created to replace HTML and XML tags more efficiently using BeautifulSoup. Rather than first parsing with BeautifulSoup and then parse again to find specific tags, pass in a SoupReplacer object into the BeautifulSoup constructor to replace tags during the initial parse of BeautifulSoup.

The original functionality of SoupReplacer comprised of simply passing in two strings: the original tag name and the replacement tag name. While it was an effecitve way of replacing one type of tag with another tag, that was as much as it could do.

The new constructor can now take in functions that either take it the tag name, tag attributes, or the tag itself. This allows for more complex replacements, as well as being able to replace multiple types of tags at once. I believe that we should implement this version of SoupReplacer as it allows for significantly more complex replacements.