# QUICK REFERENCE GUIDE

```python
import uiautomator2 as u2

d = u2.connect("--serial-here--")  # Can omit parameter if there's only one device
d = u2.connect()  # Uses ANDROID_SERIAL env var if single device

# Device Information
print(d.info)  # Get device info
print(d.device_info)  # Get detailed device info
width, height = d.window_size()  # Get screen dimensions
print(d.wlan_ip)  # Get wireless IP
print(d.serial)  # Get device serial number

# Screen Operations
d.screenshot()  # Returns Pillow.Image.Image
d.screenshot().save("current_screen.jpg")  # Save screenshot

# UI Hierarchy
d.dump_hierarchy()  # Returns hierarchy as XML string

# Wait Settings
d.implicitly_wait(10)  # Set element search timeout (seconds)

# App Management
d.app_current()  # Get current app's packageName and activity
d.app_start("io.appium.android.apis")  # Launch app
d.app_start("io.appium.android.apis", stop=True)  # Stop then launch app
d.app_stop("io.appium.android.apis")  # Stop app

# Session Management
app = d.session("io.appium.android.apis")  # Start app session
# Sessions monitor app crashes - throws SessionBrokenError if app crashes
app.click(10, 20)  # Click coordinates in session

# Touch Actions (No Session)
d.click(10, 20)  # Click coordinates
d.long_click(10, 10)  # Long press
d.double_click(10, 20)  # Double click

# Gesture Actions
d.swipe(10, 20, 80, 90)  # Swipe from (10,20) to (80,90)
d.swipe_ext("right")  # Full screen swipe right
d.swipe_ext("right", scale=0.9)  # Swipe right 90% of screen width
d.drag(10, 10, 80, 80)  # Drag operation

# System Keys
d.press("back")  # Press back button
d.press("home")  # Press home button
d.long_press("volume_up")  # Long press volume up

# Text Input
d.send_keys("hello world")  # Type text (requires active input field)
d.clear_text()  # Clear input field

# Screen Control
d.screen_on()  # Wake up device
d.screen_off()  # Sleep device

# Screen Orientation
print(d.orientation)  # Get orientation (left|right|natural|upsidedown)
d.orientation = 'natural'  # Set orientation
d.freeze_rotation(True)  # Lock rotation

# System UI
print(d.last_toast)  # Get last toast message
d.clear_toast()  # Clear toast history

d.open_notification()  # Open notification panel
d.open_quick_settings()  # Open quick settings

d.open_url("https://www.bing.com")  # Open URL
d.keyevent("HOME")  # Send keyevent

# Shell Commands
output, exit_code = d.shell("ps -A", timeout=60)  # Execute shell command
output = d.shell("pwd").output  # Get command output
exit_code = d.shell("pwd").exit_code  # Get exit code

# Selector Operations
sel = d(text="Gmail")  # Create selector
sel.wait()  # Wait for element
sel.click()  # Click element
```

```python
# XPath Operations
d.xpath("Open Account").wait()  # Wait for element (default 10s)
d.xpath("Open Account").wait(timeout=10)  # Custom timeout

# Common Settings
d.settings['wait_timeout'] = 20  # Default element search timeout (20s)

# Complex XPath Operations
d.xpath("Open Account").click()  # Wait and click
d.xpath("//*[@text='FM']/../android.widget.ImageView").click()  # Complex path
d.xpath('//*[@text="FM"]').get().info  # Get element info

# Element Collection Operations
for el in d.xpath('//android.widget.EditText').all():
    print("rect:", el.rect)  # (left_x, top_y, width, height)
    print("bounds:", el.bounds)  # (left, top, right, bottom)
    print("center:", el.center())  # Get center coordinates
    el.click()  # Click element
    print(el.elem)  # Print lxml Node

# Watcher (Monitor popups in thread)
d.watcher.when("Skip").click()  # Set up watcher
d.watcher.start()  # Start watching
```

More comments are welcome. **Pull Requests are more than welcome**
