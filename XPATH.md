# uiautomator2 XPath Extension

Before using this plugin, it's essential to have some basic knowledge of XPath. Fortunately, there is plenty of online material available on this topic. Here are some resources:

- [W3CSchool XPath Tutorial](http://www.w3school.com.cn/xpath/index.asp)
- [XPath Tutorial](http://www.zvon.org/xxl/XPathTutorial/)
- [Ruanyifeng's XPath Learning Notes](http://www.ruanyifeng.com/blog/2009/07/xpath_path_expressions.html)
- [XPath Testing Website](https://www.freeformatter.com/xpath-tester.html)
- [XPath Tester](https://extendsclass.com/xpath-tester.html)

The code has not been fully tested, so there may still be bugs. Feel free to provide feedback.

## How It Works

1. Using the `dump_hierarchy` interface of the uiautomator2 library, the current UI screen is obtained (a rich XML structure).
2. Then, the `lxml` library is used to parse the XML, search for matching XPath expressions, and perform actions like clicking.

> Currently, it has been found that lxml only supports XPath 1.0. If you know how to support XPath 2.0, feel free to share.

**Popup Monitoring Principle**

Through the hierarchy, we can gather information about all the elements on the screen (including popups and clickable buttons). Let's assume there are two popup buttons: `Skip` and `Got it`. The button we want to click is `Play`.

1. Get the current screen’s XML (using the `dump_hierarchy` function).
2. Check for the existence of `Skip` and `Got it` buttons. If they exist, click them, and then return to step 1.
3. Check for the `Play` button. If found, click it and finish. If not found, return to step 1 and keep executing until the search count exceeds the limit.

## Installation

```shell
pip3 install -U uiautomator2
```

## Usage

### Basic Usage

Refer to the simple example below to understand how to use it.

```python
import uiautomator2 as u2

def main():
    d = u2.connect()
    d.app_start("com.netease.cloudmusic", stop=True)

    d.xpath('//*[@text="Private FM"]').click()
    
    #
    # Advanced Usage (Element Positioning)
    #

    # @ at the beginning
    d.xpath('@personal-fm')  # Equivalent to d.xpath('//*[@resource-id="personal-fm"]')
    # Multiple condition positioning, similar to AND
    d.xpath('//android.widget.Button').xpath('//*[@text="Private FM"]')
    
    d.xpath('//*[@text="Private FM"]').parent()  # Position to the parent element
    d.xpath('//*[@text="Private FM"]').parent("@android:list")  # Position to the parent element matching the condition

    # When using child, avoid multi-condition XPath as it can lead to confusion
    d.xpath('@android:id/list').child('/android.widget.TextView').click()
    # Equivalent to this
    # d.xpath('//*[@resource-id="android:id/list"]/android.widget.TextView').click()
```

> For simplicity, I won’t include `import` and `main` here, assuming the variable `d` already exists.

### Operations using `XPathSelector`

```python
sl = d.xpath("@com.example:id/home_searchedit")  # `sl` is an XPathSelector object

# Click
sl.click()
sl.click(timeout=10)  # Specify timeout, raises XPathElementNotFoundError if not found
sl.click_exists()  # Click if exists, returns whether the click was successful
sl.click_exists(timeout=10)  # Wait for up to 10 seconds

sl.match()  # Returns None if not matched, otherwise returns XMLElement

# Wait for the element to appear, returns XMLElement
# Default wait time is 10 seconds
el = sl.wait()
el = sl.wait(timeout=15)  # Wait for 15 seconds, returns None if not found

# Wait for the element to disappear
sl.wait_gone()
sl.wait_gone(timeout=15) 

# Similar to wait, but if not found, raises XPathElementNotFoundError
el = sl.get()
el = sl.get(timeout=15)

# Change default wait time to 15 seconds
d.xpath.global_set("timeout", 15)
d.xpath.implicitly_wait(15)  # Equivalent to the previous line of code (TODO: Removed)

print(sl.exists)  # Returns whether it exists (bool)
sl.get_last_match()  # Get the last matched XMLElement

sl.get_text()  # Get component name
sl.set_text("")  # Clear the input box
sl.set_text("hello world")  # Enter "hello world" into the input box

# Iterate over all matched elements
for el in d.xpath('//android.widget.EditText').all():
    print("rect:", el.rect)  # Output tuple: (x, y, width, height)
    print("center:", el.center())
    el.click()  # Click operation
    print(el.elem)  # Output the Node parsed by lxml
    print(el.text)

# Child operation
d.xpath('@android:id/list').child('/android.widget.TextView').click()
# Equivalent to d.xpath('//*[@resource-id="android:id/list"]/android.widget.TextView').all()
```

Advanced Search Syntax

> Added in version 3.1

```python
# Search for text=NFC AND id=android:id/item
(d.xpath("NFC") & d.xpath("@android:id/item")).get()

# Search for text=NFC OR id=android:id/item
(d.xpath("NFC") | d.xpath("App") | d.xpath("Content")).get()

# More complex queries are also supported
((d.xpath("NFC") | d.xpath("@android:id/item")) & d.xpath("//android.widget.TextView")).get()
```

### Operations with `XMLElement` ###

```python
# The object returned by XPathSelector.get() is called XMLElement
el = d.xpath("@com.example:id/home_searchedit").get()

lx, ly, width, height = el.rect  # Get top-left coordinates and width/height
lx, ly, rx, ry = el.bounds  # Get top-left and bottom-right coordinates
x, y = el.center()  # Get element center position
x, y = el.offset(0.5, 0.5)  # Same as center()

# Send click
el.click()

# Print text content
print(el.text) 

# Get attributes within the element as a dictionary
print(el.attrib)

# Screenshot of the element (principle: capture full screenshot, then crop)
el.screenshot()

# Element swipe
el.swipe("right")  # left, right, up, down
el.swipe("right", scale=0.9)  # scale is 0.9 by default, meaning the swipe distance is 90% of the element's width, or 90% of its height when swiping up

print(el.info)
# Example output
{'index': '0',
 'text': '',
 'resourceId': 'com.example:id/home_searchedit',
 'checkable': 'true',
 'checked': 'true',
 'clickable': 'true',
 'enabled': 'true',
 'focusable': 'false',
 'focused': 'false',
 'scrollable': 'false',
 'longClickable': 'false',
 'password': 'false',
 'selected': 'false',
 'visibleToUser': 'true',
 'childCount': 0,
 'className': 'android.widget.Switch',
 'bounds': {'left': 882, 'top': 279, 'right': 1026, 'bottom': 423},
 'packageName': 'com.android.settings',
 'contentDescription': '',
 'resourceName': 'android:id/switch_widget'}

```

### Scroll to a Specific Position

> `scroll_to` is a newly added feature and may not be fully refined (e.g., it doesn't detect when you've scrolled to the bottom).

Check the example first

```python
from uiautomator2 import connect_usb, Direction

d = connect_usb()

d.scroll_to("Place Order")
d.scroll_to("Place Order", Direction.FORWARD) # Default scrolls downwards, can also be BACKWARD, HORIZ_FORWARD(horizontal), HORIZ_BACKWARD(horizontal reverse)
d.scroll_to("Place Order", Direction.HORIZ_FORWARD, max_swipes=5)

# It can also scroll within a specific element
d.xpath('@com.taobao.taobao:id/dx_root').scroll(Direction.HORIZ_FORWARD)
d.xpath('@com.taobao.taobao:id/dx_root').scroll_to("Place Order", Direction.HORIZ_FORWARD)
```

**A More Complete Example**

```python
import uiautomator2 as u2
from uiautomator2 import Direction

def main():
    d = u2.connect()
    d.app_start("com.netease.cloudmusic", stop=True)

    # Steps
    d.xpath("//*[@text='Personal FM']/../android.widget.ImageView").click()
    d.xpath("Next song").click()

    # Monitor popups for 2 seconds, actual time may exceed 2 seconds
    d.xpath.sleep_watch(2)
    d.xpath("Back to the previous level").click()
    
    d.xpath("Back to the previous level").click(watch=False) # Click without triggering watch
    d.xpath("Back to the previous level").click(timeout=5.0) # Wait timeout for 5s

    d.xpath.watch_background() # Open background monitoring mode, checks every 4s by default
    d.xpath.watch_background(interval=2.0) # Check every 2s
    d.xpath.watch_stop() # Stop monitoring

    for el in d.xpath('//android.widget.EditText').all():
        print("rect:", el.rect) # Output tuple: (left_x, top_y, width, height)
        print("bounds:", el.bounds) # Output tuple: (left, top, right, bottom)
        print("center:", el.center())
        el.click() # Click operation
        print(el.elem) # Outputs Node parsed by lxml
    
    # Swipe
    el = d.xpath('@com.taobao.taobao:id/fl_banner_container').get()

    # Swipe from right to left
    el.swipe(Direction.HORIZ_FORWARD) 
    el.swipe(Direction.LEFT) # Swipe from right to left

    # Swipe from bottom to top
    el.swipe(Direction.FORWARD)
    el.swipe(Direction.UP)

    el.swipe("right", scale=0.9) # Default scale is 0.9, swipe distance is 80% of the control's width, swipe center is consistent with control's center
    el.swipe("up", scale=0.5) # Swipe distance is 50% of the control's height

    # Scroll is different from swipe, scroll returns a bool indicating if there's a new element appearing
    el.scroll(Direction.FORWARD) # Scroll down
    el.scroll(Direction.BACKWARD) # Scroll up
    el.scroll(Direction.HORIZ_FORWARD) # Scroll horizontally forward
    el.scroll(Direction.HORIZ_BACKWARD) # Scroll horizontally backward

    if el.scroll("forward"):
        print("Can continue scrolling")
```

### `PageSource` Object
> Added in version 3.1

This is an advanced usage, but this object is the most basic; almost all functions depend on it.

What is PageSource?

PageSource is initialized from the return value of `d.dump_hierarchy()`. It's primarily used for finding elements via XPath.

How to use it?

```python
source = d.xpath.get_page_source()

# find_elements is the core method
elements = source.find_elements('//android.widget.TextView') # List[XMLElement]
for el in elements:
    print(el.text)

# Obtain coordinates and then click
x, y = elements[0].center()
d.click(x, y)

# Various condition query writing
es1 = source.find_elements('//android.widget.TextView')
es2 = source.find_elements(XPath('@android:id/content').joinpath("//*"))

# Find nodes that are TextViews but not under id=android:id/content
els = set(es1) - set(es2)

# Find nodes that are TextViews and belong to id=android:id/content
els = set(es1) & set(es2)
```

## XPath Rules
To write scripts faster, we have customized some simplified XPath rules.

**Rule 1**

`//` at the start represents the native XPath

**Rule 2**

`@` at the start represents resourceId positioning

`@smartisanos:id/right_container` is equivalent to 
`//*[@resource-id="smartisanos:id/right_container"]`

**Rule 3**

`^` at the start represents regular expressions

`^.*Got it` is equivalent to `//*[re:match(text(), '^.*Got it')]`

**Rule 4**

> Inspired by SQL "like"

`Know%` matches text starting with `Know`, equivalent to `//*[starts-with(text(), 'Know')]`

`%Know` matches text ending with `Know`, equivalent to `//*[ends-with(text(), 'Know')]`

`%Know%` matches text containing `Know`, equivalent to `//*[contains(text(), 'Know')]`

**Rule Last**

Matches text and description fields.

For example, `Search` is equivalent to XPath `//*[@text="Search" or @content-desc="Search" or @resource-id="Search"]`

## Special Notes
- Sometimes className may contain `$@#&` characters, which are illegal in XML, so they are all replaced with `.`

## Some Advanced XPath Usages
```
# All elements
//*

# resource-id contains the string 'login'
//*[contains(@resource-id, 'login')]

# Button contains 'account' or 'accounts'
//android.widget.Button[contains(@text, 'account') or contains(@text, 'accounts')]

# The second ImageView among all ImageViews
(//android.widget.ImageView)[2]

# The last ImageView among all ImageViews
(//android.widget.ImageView)[last()]

# className contains ImageView
//*[contains(name(), "ImageView")]
```

## Some Useful Websites
- [XPath playground](https://scrapinghub.github.io/xpath-playground/)
- [Advanced XPath Usage on Jianshu](https://www.jianshu.com/p/4fef4142b33f)
- [XPath Quicksheet](https://devhints.io/xpath)

If you have other materials, feel free to submit [Issues](https://github.com/openatx/uiautomator2/issues/new) for supplementation.