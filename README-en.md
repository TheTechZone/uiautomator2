# uiautomator2
![PyPI](https://img.shields.io/pypi/v/uiautomator2.svg)[](https://pypi.python.org/pypi/uiautomator2)
![PyPI](https://img.shields.io/pypi/pyversions/uiautomator2.svg)
![codecov](https://codecov.io/gh/openatx/uiautomator2/graph/badge.svg?token=d0ZLkqorBu)[](https://codecov.io/gh/openatx/uiautomator2)

QQ chat group: **815453846 Discord**: https://discord.gg/PbJhnZJKDd
> I haven't maintained this project for a while (maybe two years), but recently I needed to study Android native automation again for work, and of course I also looked into Appium. After comparing them, I found that the running speed of the uiautomator2 project is really fast, from detecting elements to clicking, it is all in milliseconds, and the code is also easier to understand. I never thought that I had written such a magical project before. How could such a good project be left to gather dust? I need to tidy it up and clean up some junk code. So the project version was upgraded from 2.xx to 3.xx

Users who are still using version 2.xx can take a look[docs/2to3.md](docs/2to3.md) at 2to3 before deciding whether to upgrade to 3.xx (I personally still strongly recommend upgrading)

After all, the upgrade from 2 to 3 is a major version upgrade, and many functions have been deleted. The first thing to delete is atx-agent, and then there are a bunch of atx-agent related functions. Deprecated functionality such as init.

Version numbers of various dependent libraries

- ![PyPI](https://img.shields.io/pypi/v/uiautomator2.svg?label=uiautomator2)[](https://pypi.python.org/pypi/uiautomator2)
- ![PyPI](https://img.shields.io/pypi/v/adbutils.svg?label=adbutils)[](https://github.com/openatx/adbutils)
- ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/openatx/android-uiautomator-server.svg?label=android-uiautomator-server)[](https://github.com/openatx/android-uiautomator-server)
- ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/openatx/atx-agent.svg?label=atx-agent)[](https://github.com/openatx/atx-agent)

[UiAutomator](https://developer.android.com/training/testing/ui-automator.html) is a Java library provided by Google for Android automated testing, based on the Accessibility service. It is very powerful and can test third-party apps, obtain the properties of any control of any app on the screen, and perform arbitrary operations on it, but it has two disadvantages: 1. Test scripts can only use Java 2. The test script must be packaged into a jar or apk package and uploaded to the device before it can be run.

We hope that the test logic can be written in Python and can control the phone when running on the computer. Many thanks to Xiaocong He ([@xiaocong][]), who implemented this idea[ (see](https://github.com/xiaocong/uiautomator) xiaocong/uiautomator) by running an http rpc service on the phone, opening up the functions in uiautomator, and then encapsulating these http interfaces into a Python library. 
Because the `xiaocong/uiautomator library` has not been updated for a long time. <https://github.com/openatx/uiautomator2><https://github.com/openatx/android-uiautomator-server>So we forked a version directly. In order to distinguish it, we added a 2 openatx/uiautomator2 at the end. I also forked the corresponding Android package source code, openatx/android-uiautomator-server

In addition to fixing the bugs in the original library, many new features have been added. The main parts are as follows:

* ~~The device<https://github.com/openatx/atx-agent> and the development machine can be disconnected from the data cable and connected via WiFi (based on atx-agent~~
* [~~Integrates openstf/](https://github.com/openstf/minicap)~~minicap to achieve real-time screen projection and real-time screenshots~~
* [~~Integrates openstf/minitouch to ](https://github.com/openstf/minitouch)~~achieve precise real-time control of devices~~
* Fixed the frequent exit issue[ ](https://github.com/xiaocong/uiautomator)of xiaocong/uiautomator
* The code has been refactored and streamlined for easy maintenance
* Implemented a device management platform (also supports iOS) [atxserver2](https://github.com/openatx/atxserver2) (Note: currently not maintained)
* Expanded toast acquisition and display functions (need to manually enable ATX floating window permissions) It seems that there is a bug and it cannot be used
> I would like to explain this first, because many people often ask that [openatx/uiautomator2 does](https://github.com/openatx/facebook-wda) not support iOS testing. If you need iOS automated testing, you can turn to this library openatx/facebook-wda.

> PS: This library [~~https://github.com/NeteaseGame/ATX is~~](https://github.com/NeteaseGame/ATX) currently out of maintenance, please switch to it as soon as possible.

Here is a [quick reference guide for](./QUICK_REFERENCE.md) those who are already getting started. Please give us your comments.
## Requirements
- Android version 4.4+
- Python 3.8+
## QUICK START
First prepare `an Android` phone (not two) with developer options turned on, connect it to the computer, and make sure that the connected device can be seen by executing adb devices.

`Run pip3 install -U uiautomator2 to` install uiautomator2

Run Python on the command line to open the Python interactive window. Then enter the following command into the window.
```python
import uiautomator2 as u2

d = u2.connect() # connect to device
print(d.info)
```

When you see output similar to the following, you can officially start using our library. Because this library has too many functions, there is still a lot of content to come, so you need to read it slowly...
```
{'currentPackageName': 'net.oneplus.launcher', 'displayHeight': 1920, 'displayRotation': 0, 'displaySizeDpX': 411, 'displaySizeDpY': 731, 'displayWidth': 1080, 'productName': 'OnePlus5', '
screenOn': True, 'sdkInt': 27, 'naturalOrientation': True}
```

`In addition`, in order to maintain stability, you also need to enable the floating window permission of the shared bike. Reference article py-uiautomator2 makes [the service](https://zhuanlan.zhihu.com/p/688009468) available for a long time through floating windows

Generally it will be successful, but there may be unexpected situations. You can join the QQ group to report problems (the group number is at the top). There are many big guys in the group who can help you solve the problem.
## Sponsors
Thank you to all our sponsors! ✨🍰✨
### Gold Sponsor
Empty
# Article Recommended
Recommended excellent articles (feedback is welcome in the QQ group)

- [https://www.cnblogs.com/ze-yan/p/12242383.html`](https://www.cnblogs.com/ze-yan/p/12242383.html)`How to deploy uiautomator2 in termux by Chengdu-testing only a little bit`
## Related Projects
- [Adbutils library](https://github.com/openatx/adbutils) for interacting with Android based on adb protocol
- [uiauto.dev](https://uiauto.dev) is used to view the UI hierarchy structure, similar to uiautomatorviewer (used to replace the previously written weditor), used to view the UI hierarchy structure
- Device management platform, [when](https://github.com/openatx/atxserver2) there are more devices, atxserver2 will be used (looking for project maintainers)
- [~~atx-agent](https://github.com/openatx/atx-agent) ~~is a daemon program running on the device, developed in Go, used to keep related services on the device alive~~
- [~~weditor is](https://github.com/openatx/weditor) ~~similar to uiautomatorviewer, an auxiliary editor developed specifically for this project (this one is not maintained yet~~

[**Installation**](#installation)

[**Connect to a device**](#connect-to-a-device)

[**Command line**](#command-line)

[**Global settings**](#global-settings)

- [**Debug HTTP requests**](#debug-http-requests)
- [**Implicit wait**](#implicit-wait)

[**App management**](#app-management)

- [**Install an app**](#install-an-app)
- [**Launch an app**](#launch-an-app)
- [**Stop an app**](#stop-an-app)
- [**Stop all running apps**](#stop-all-running-apps)
- [**Push and pull files**](#push-and-pull-files)
- [**Other app operations**](#other-app-operations)

[**UI automation**](#basic-api-usages)

- [**Shell commands**](#shell-commands)
- [**Session**](#session)
- [**Retrieve the device info**](#retrieve-the-device-info)
- [**Key Events**](#key-events)
- [**Gesture interaction with the device**](#gesture-interaction-with-the-device)
- [**Screen-related**](#screen-related)
- [**Selector**](#selector)
- [**Watcher**](#watcher)
- [**Global settings**](#global-settings)
- [**Input method**](#input-method)
- [**Toast**](#toast)
- [**XPath**](#xpath)
- [**Screenrecord**](#screenrecord)
- [**Image match](#image-match) **Removed**

[**Contributors**](#contributors)

[**LICENSE**](#license)
# Installation
1. Install uiautomator2
   ```shell
   pip install -U uiautomator2
   ```

   `Test whether the `installation is successful `uiautomator2 --help`
1. UI Inspector
   ```shell
   pip install uiautodev
   # 
   Start uiauto.dev
   ```

   Open https://uiauto.dev in your browser to view the interface structure of the current device.

   **uiauto.dev**

   [uiauto.dev is](https://github.com/codeskyblue/uiauto.dev) a project independent of uiautomator2, used to view the layer structure. This is [a refactored version](https://github.com/openatx/weditor) of the old project weditor. It may be charged later (the price is definitely worth it) to support the continued maintenance of the current project. If you are interested, you can join the group to discuss (including raising requirements) QQ group 536481989
# Connect to a device
use serialno to connect device eg. `123456f` (seen from `adb devices`)
```python
import uiautomator2 as u2

d = u2.connect('123456f') # alias for u2.connect_usb('123456f')
print(d.info)
```

Serial can be passed through env-var `ANDROID_SERIAL`
```python
# export ANDROID_SERIAL=123456f
d = u2.connect()
```
# Command line
Where` $device_`ip represents the IP address of the device

`If you need to specify a device, you need to pass in --serial, such as python3 -m uiautomator2 --serial bff1234 SubCommand, SubCommand is the subcommand (screenshot, current, etc.)`
> 1.0.3 Added: `python3 -m uiautomator2` equals to `uiautomator2`

- screenshot: screenshot
  ```bash
  $ uiautomator2 screenshot screenshot.jpg
  ```
- current: Get the current package name and activity
  ```bash
  $ uiautomator2 current
  {
      "package": "com.android.browser",
      "activity": "com.uc.browser.InnerUCMobile",
      "pid": 28478
  }
  ```
- uninstall： Uninstall app
  ```bash
  $ uiautomator2 uninstall<package-name> # Uninstall a package
   $ uiautomator2 uninstall<package-name-1><package-name-2> # Uninstall multiple packages
   $ uiautomator2 uninstall --all # Uninstall all
  ```
- stop: Stop app
  ```bash
  $ uiautomator2 stop com.example.app # Stop an
   app $ uiautomator2 stop --all # Stop all apps
  ```
- doctor:
  ```bash
  $ uiautomator2 doctor
  [I 2024-04-25 19:53:36,288 __main__:101 pid:15596] uiautomator2 is OK
  ```
# API Documents
### ~~New command timeout （Removed)~~
When Python quits, the UiAutomation service also quits. 
<!-- How long (in seconds) will wait for a new command from the client before assuming the client quit and ending the uiautomator service （Default 3 minutes）

Configure the maximum idle time of the accessibility service. The service will be automatically released after a timeout. The default value is 3 minutes.
```python
d.set_new_command_timeout(300) # change to 5 minutes, unit seconds
```-->

### Debug HTTP requests 

Print out the HTTP request information behind the code

```python
>>> d.debug = True
>>> d.info
12:32:47.182 $ curl -X POST -d '{"jsonrpc": "2.0", "id": "b80d3a488580be1f3e9cb3e926175310", "method": "deviceInfo", "params": {}}' 'http://127.0.0.1:54179/jsonrpc/0'
12:32:47.225 Response >>>
{"jsonrpc":"2.0","id":"b80d3a488580be1f3e9cb3e926175310","result":{"currentPackageName":"com.android.mms","displayHeight":1920,"displayRotation":0,"displaySizeDpX":360,"displaySizeDpY":640,"displayWidth":1080,"productName"
:"odin","screenOn":true,"sdkInt":25,"naturalOrientation":true}}
<<< END
```

### Implicit wait
Set the element search waiting time (default 20s)
```python
d.implicitly_wait(10.0) # You can also modify through d.settings['wait_timeout'] = 10.0
d(text="Settings").click()  # if Settings button not shown in 10s, UiObjectNotFoundError will be raised

print("wait timeout" , d.implicitly_wait()) # get default implicit wait
```


This function will have influence on `click`, `long_click`, `drag_to`, `get_text`, `set_text`, `clear_text`, etc.

## App management
This part showcases how to perform app management

### Install an app
We only support installing an APK from a URL

```python
d.app_install('http://some-domain.com/some.apk')
```

### Launch an app

```python
# The default method is to parse the mainActivity of the apk package through atx-agent, and then call am start -n $package/$activity to start 
d.app_start("com.example.hello_world") 

# Use monkey -p com.example.hello_world -c android.intent.category.LAUNCHER 1 to start 
# This method has a side effect, it will automatically turn off the phone's rotation lock 
d.app_start("com.example.hello_world", use_monkey=True) # start with package name 

# Starting the application by specifying the main activity is equivalent to calling am start -n com.example.hello_world/.MainActivity 
d.app_start("com.example.hello_world", ".MainActivity")
```

### Stop an app

```python
# equivalent to `am force-stop`, thus you could lose data
d.app_stop("com.example.hello_world") 
# equivalent to `pm clear`
d.app_clear('com.example.hello_world')
```

### Stop all running apps
```python
# stop all
d.app_stop_all()
# stop all app except for com.examples.demo
d.app_stop_all(excludes=['com.examples.demo'])
```
### Get app info

```python
d.app_info("com.examples.demo")
# expect output
#{
#    "mainActivity": "com.github.uiautomator.MainActivity",
#    "label": "ATX",
#    "versionName": "1.1.7",
#    "versionCode": 1001007,
#    "size":1760809
#}

# save app icon
img = d.app_icon("com.examples.demo")
img.save("icon.png")
```

### List all running apps

```python
d.app_list_running()
# expect output
# ["com.xxxx.xxxx", "com.github.uiautomator", "xxxx"]
```
### Wait until app is running

```python
pid = d.app_wait("com.example.android") # Wait for the application to run, return pid(int)
if not pid:
  print("com.example.android is not running")
else: 
  print("com.example.android pid is %d" % pid)

d.app_wait("com.example.android", front=True) # Wait for the application to run in the foreground
d.app_wait("com.example.android", timeout=20.0) # Maximum waiting time 20s (default)
```

> Added in version 1.2.0

### Push and pull files
* push a file to the device

```python
# push to a folder
d.push("foo.txt", "/sdcard/")
# push and rename
d.push("foo.txt", "/sdcard/bar.txt")
# push fileobj
with open("foo.txt", 'rb') as f:
  d.push(f, "/sdcard/")
# push and change file access mode
d.push("foo.sh", "/data/local/tmp/", mode=0o755)
```
  
* pull a file from the device

```python
d.pull("/sdcard/tmp.txt", "tmp.txt")

# FileNotFoundError will raise if the file is not found on the device
d.pull("/sdcard/some-file-not-exists.txt", "tmp.txt")
```
  
### Other app operations

```python
# grant all the permissions
d.app_auto_grant_permissions("io.appium.android.apis")

# open scheme
d.open_url("appname://appnamehost")
# same as
# adb shell am start -a android.intent.action.VIEW -d "appname://appnamehost"
```

## Basic API Usages
This part showcases how to perform common device operations:

### Shell commands
* Run a short-lived shell command with timeout protection. (Default timeout 60s)

  Note: timeout support require `atx-agent >=0.3.3`

  `adb_shell` function is deprecated. Use `shell` instead.

  Simple usage

```python
output, exit_code = d.shell("pwd", timeout=60) # timeout 60s (Default)
# output: "/\n", exit_code: 0
# Similar to command: adb shell pwd

# Since `shell` function return type is `namedtuple("ShellResponse", ("output", "exit_code"))`
# so we can do some tricks
output = d.shell("pwd").output
exit_code = d.shell("pwd").exit_code
```

The first argument can be a list, for example:
```python
output, exit_code = d.shell(["ls", "-l"])
# output: "/....", exit_code: 0
```

This returns a string for stdout merged with stderr. 
If the command is a blocking command, `shell` will also block until the command is completed or the timeout kicks in. No partial output will be received during the execution of the command. This API is not suitable for long-running commands. The shell command given runs in a similar environment of `adb shell`, which has a Linux permission level of `adb` or `shell` (higher than an app permission).

* Run a long-running shell command (Removed)
<!--
  add stream=True will return `requests.models.Response` object. More info see [requests stream](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#id5)
  
  ```python
  r = d.shell("logcat", stream=True)
  # r: requests.models.Response
  deadline = time.time() + 10 # run maxium 10s
  try:
      for line in r.iter_lines(): # r.iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)
          if time.time() > deadline:
              break
          print("Read:", line.decode('utf-8'))
  finally:
      r.close() # this method must be called
  ```

  Command will be terminated when `r.close()` called. -->

### Session
Session represents an app lifecycle. Can be used to start app or detect if the app crashes.

* Launch and close app

```python
sess = d.session("com.netease.cloudmusic") # start NetEase Cloud Music
sess.close() # stop NetEase Cloud Music
sess.restart() # cold start NetEase Cloud Music
```

* Use python `with` to launch and close app
```python
with d.session("com.netease.cloudmusic") as sess:
  sess(text="Play").click()
```
* Attach to the running app

```python
# launch app if not running, skip launch if already running
sess = d.session("com.netease.cloudmusic", attach=True)
```

* Detect app crashes

```python
# When the app is still running
sess(text="Music").click() # operation goes normal

# If the app crashes or quits
sess(text="Music").click() # raise SessionBrokenError
# other function calls under session will raise SessionBrokenError too
```

```python
# check if session is ok. 
# Warning: function name may change in the future
sess.running() # True or False
```

### Retrieve the device info

Get basic information

```python
d.info
```

Below is a possible output:

```python
{'currentPackageName': 'com.android.systemui',
 'displayHeight': 1560,
 'displayRotation': 0,
 'displaySizeDpX': 360,
 'displaySizeDpY': 780,
 'displayWidth': 720,
 'naturalOrientation': True,
 'productName': 'ELE-AL00',
 'screenOn': True,
 'sdkInt': 29}
```

Get window size

```python
print(d.window_size())
# device upright output example: (1080, 1920)
# device horizontal output example: (1920, 1080)
```

Get current app info. For some android devices, the output could be empty (see *Output example 3*)

```python
print(d.app_current())
# Output example 1: {'activity': '.Client', 'package': 'com.netease.example', 'pid': 23710}
# Output example 2: {'activity': '.Client', 'package': 'com.netease.example'}
# Output example 3: {'activity': None, 'package': None}
```

Wait activity

```python
d.wait_activity(".ApiDemos", timeout=10) # default timeout 10.0 seconds
# Output: true of false
```

Get device serial number

```python
print(d.serial)
# output example: 74aAEDR428Z9
```

Get WLAN ip
```python
print(d.wlan_ip)
# output example: 10.0.0.1 or None
```

~~Get detailed device info~~ `d.device_info`

device\_info
```python
print(d.device_info)
```

Below is a possible output:

```python
{'arch': 'arm64-v8a',
 'brand': 'google',
 'model': 'sdk_gphone64_arm64',
 'sdk': 34,
 'serial': 'EMULATOR34X1X19X0',
 'version': 14}
```

### Clipboard
Get of set clipboard content

Set or get the content of the pasteboard

* clipboard/set\_clipboard

```python
d.clipboard = 'hello-world'
# or
d.set_clipboard('hello-world', 'label')
```

Get clipboard content

> get clipboard requires IME(com.github.uiautomator/.AdbKeyboard) call `d.set_input_ime()` before using it.

```python
# get clipboard content
print(d.clipboard)
```

### Key Events
* Turn screen on/off
* 
```python
d.screen_on() # turn on the screen
d.screen_off() # turn off the screen
```

* Get current screen status

```python
d.info.get('screenOn') # require Android >= 4.4
```

* Press hard/soft key

```python
d.press("home") # press the home key, with key name
d.press("back") # press the back key, with key name
d.press(0x07, 0x02) # press keycode 0x07('0') with META ALT(0x02)
```

* These key names are currently supported:
  - home
  - back
  - left
  - right
  - up
  - down
  - center
  - menu
  - search
  - enter
  - delete ( or del)
  - recent (recent apps)
  - volume\_up
  - volume\_down
  - volume\_mute
  - camera
  - power

You can find all key code definitions at [Android KeyEvnet](https://developer.android.com/reference/android/view/KeyEvent.html)

* Unlock screen

```python
d.unlock()
# This is equivalent to
# 1. press("power")
# 2. swipe from left-bottom to right-top
```

### Gesture interaction with the device
* Click on the screen

```python
d.click(x, y)
```

* Double click

```python
d.double_click(x, y)
d.double_click(x, y, 0.1) # default duration between two click is 0.1s
```

* Long click on the screen

```python
d.long_click(x, y)
d.long_click(x, y, 0.5) # long click 0.5s (default)
```

* Swipe

```python
d.swipe(sx, sy, ex, ey)
d.swipe(sx, sy, ex, ey, 0.5) # swipe for 0.5s(default)
```

* SwipeExt extension
```python
d.swipe_ext("right") # Swipe right, choose 1 from 4 options: "left", "right", "up", "down"
d.swipe_ext("right", scale=0.9) # Default is 0.9, the sliding distance is 90% of the screen width
d.swipe_ext("right", box=(0, 0, 100, 100)) # Swipe in the area (0,0) -> (100, 100) #

# In practice, it is found that when swiping up or down, the success rate of sliding from the midpoint will be higher
d.swipe_ext("up", scale=0.8) # Code will be vkk# You can also use Direction as a parameter 

from uiautomator2 import Direction
d.swipe_ext(Direction.FORWARD) # Scroll down, equivalent to d.swipe_ext("up"), but easier to understand
d.swipe_ext(Direction.BACKWARD) # d.swipe_ext(Direction.HORIZ_FORWARD) # Page flips horizontally to the right 
d.swipe_ext(Direction.HORIZ_BACKWARD) # Page flips horizontally to the left
```

* Drag
```python
d.drag(sx, sy, ex, ey)
d.drag(sx, sy, ex, ey, 0.5) # swipe for 0.5s(default)
```

* Swipe points
```python
# swipe from point(x0, y0) to point(x1, y1) then to point(x2, y2)
# time will speed 0.2s between two points
d.swipe_points([(x0, y0), (x1, y1), (x2, y2)], 0.2))
```

It is mostly used for Jiugongge unlocking, and the relative coordinates of each point are obtained in advance (percentage is supported here). For more detailed usage, please refer to this post to use u2 to realize [Jiugongge pattern unlocking][https://testerhome.com/topics/11034]

* Touch and drap (Beta)

* This interface is a relatively low-level primitive interface. It doesn’t seem to be perfect, but it can be used. Note: This place does not support percentages

```python
d.touch.down(10, 10) # simulate pressing 
time.sleep(.01) # delay between down and move, control it yourself
d.touch.move(15, 15) # simulate moving
d.touch.up(10, 10) # simulate lifting
```

Note: click, swipe, drag operations support percentage position values. Example:

`d.long_click(0.5, 0.5)` means long click center of screen

### Screen-related
* Retrieve/Set device orientation

  The possible orientations:
  - `natural` or `n`
  - `left` or `l`
  - `right` or `r`
  - `upsidedown` or `u` (can not be set)

```python
# retrieve orientation. the output could be "natural" or "left" or "right" or "upsidedown"
orientation = d.orientation

# WARNING: did not pass testing in my TT-M1
# set orientation and freeze rotation. 
# notes: setting "upsidedown" requires Android>=4.3. 
d.set_orientation('l') # or "left"
d.set_orientation("l") # or "left"
d.set_orientation("r") # or "right"
d.set_orientation("n") # or "natural"
```

* Freeze/Un-freeze rotation

```python
# freeze rotation
d.freeze_rotation()
# un-freeze rotation
d.freeze_rotation(False)
```

* Take screenshot

```python
# take screenshot and save to a file on the computer, require Android>=4.2. 
d.screenshot("home.jpg")

# get PIL.Image formatted images. Naturally, you need pillow installed first
image = d.screenshot() # default format="pillow"
image.save("home.jpg") # or home.png. Currently, only png and jpg are supported

# get opencv formatted images. Naturally, you need numpy and cv2 installed first
import cv2
image = d.screenshot(format='opencv')
cv2.imwrite('home.jpg', image)

# get raw jpeg data
imagebin = d.screenshot(format='raw')
open("some.jpg", "wb").write(imagebin)
```

* Dump UI hierarchy
```python
# get the UI hierarchy dump content
xml = d.dump_hierarchy()

# compressed=True: do not include import nodes
# pretty: format xml
# max_depth: limit xml depth, default 50
xml = d.dump_hierarchy(compressed=False, pretty=False, max_depth=50)
```

* Open notification or quick settings

```python
d.open_notification()
d.open_quick_settings()
```

### Selector

Selector is a handy mechanism to identify a specific UI object in the current window.

```python
# Select the object with text 'Clock' and its className is 'android.widget.TextView'
d(text='Clock', className='android.widget.TextView')
```

Selector supports below parameters. Refer to [UiSelector Java doc](http://developer.android.com/tools/help/uiautomator/UiSelector.html) for detailed information.

* `text`, `textContains`, `textMatches`, `textStartsWith`
* `className`, `classNameMatches`
* `description`, `descriptionContains`, `descriptionMatches`, `descriptionStartsWith`
* `checkable`, `checked`, `clickable`, `longClickable`
* `scrollable`, `enabled`,`focusable`, `focused`, `selected`
* `packageName`, `packageNameMatches`
* `resourceId`, `resourceIdMatches`
* `index`, `instance`

#### Children and siblings
* children

```python
# get the children or grandchildren
d(className="android.widget.ListView").child(text="Bluetooth")
```

* siblings
```python
# get siblings
d(text="Google").sibling(className="android.widget.ImageView")
```

* children by text or description or instance
```python
# get the child matching the condition className="android.widget.LinearLayout"
# and also its children or grandchildren with text "Bluetooth"
d(className="android.widget.ListView", resourceId="android:id/list") \
.child_by_text("Bluetooth", className="android.widget.LinearLayout")

# get children by allowing scroll search
d(className="android.widget.ListView", resourceId="android:id/list") \
.child_by_text(
    "Bluetooth",
    allow_scroll_search=True,
    className="android.widget.LinearLayout"
)
```

  - `child_by_description` is to find children whose grandchildren have
    the specified description, other parameters being similar to `child_by_text`.

  - `child_by_instance` is to find children with has a child UI element anywhere within
    ` `its sub hierarchy that is at the instance specified. It is performed on
    ` `visible views **without scrolling**.

  See below links for detailed information:
  - [UiScrollable](http://developer.android.com/tools/help/uiautomator/UiScrollable.html), `getChildByDescription`, `getChildByText`, `getChildByInstance`
  - [UiCollection](http://developer.android.com/tools/help/uiautomator/UiCollection.html), `getChildByDescription`, `getChildByText`, `getChildByInstance`

  Above methods support chained invoking, e.g. for the hierarchy below

  ```xml
  <node index="0" text="" resource-id="android:id/list" class="android.widget.ListView" ...>
  <node index="0" text="WIRELESS & NETWORKS" resource-id="" class="android.widget.TextView" .../>
  <node index="1" text="" resource-id="" class="android.widget.LinearLayout" ...>
      <node index="1" text="" resource-id="" class="android.widget.RelativeLayout" ...>
        <node index="0" text="Wi‑Fi" resource-id="android:id/title" class="android.widget.TextView" .../>
      </node>
      <node index="2" text="ON" resource-id="com.android.settings:id/switchWidget" class="android.widget.Switch" .../>
  </node>
  ...
  </node>
  ```

  ![settings](https://raw.github.com/xiaocong/uiautomator/master/docs/img/settings.png)

  To click the switch widget right to the TextView 'Wi‑Fi', we need to select the switch widgets first. However, according to the UI hierarchy, more than one switch widgets exist and have almost the same properties. Selecting by className will not work. Alternatively, the below selecting strategy would help:

```python
d(className="android.widget.ListView", resourceId="android:id/list") \
.child_by_text("Wi‑Fi", className="android.widget.LinearLayout") \
.child(className="android.widget.Switch") \
.click()
```

* relative positioning

  Also, we can use the relative positioning methods to get the view: `left`, `right`, `top`, `bottom`.

  - `d(A).left(B)`, selects B on the left side of A.
  - `d(A).right(B)`, selects B on the right side of A.
  - `d(A).up(B)`, selects B above A.
  - `d(A).down(B)`, selects B under A.

  So for the cases above, we can alternatively select it with:

```python
## select "switch" on the right side of "Wi‑Fi"
d(text="Wi‑Fi").right(className="android.widget.Switch").click()
```

* Multiple instances

  Sometimes the screen may contain multiple views with the same properties, e.g. text, then you will
  have to use the "instance" property in the selector to pick one of qualifying instances, like below:

```python
d(text="Add new", instance=0)  # which means the first instance with text "Add new"
```

  In addition, uiautomator2 provides a list-like API (similar to jQuery):

```python
# get the count of views with text "Add new" on the current screen
d(text="Add new").count

# same as count property
len(d(text="Add new"))

# get the instance via index
d(text="Add new")[0]
d(text="Add new")[1]
...

# iterator
for view in d(text="Add new"):
    view.info  # ...
```

  **Notes**: when using selectors in a code block that iterates through the result list, you must ensure that the UI elements on the screen
  keep unchanged. Otherwise, when Element-Not-Found error could occur when iterating through the list.

#### Get the selected UI object status and its information

* Check if the specific UI object exists
```python
d(text="Settings").exists # True if exists, else False
d.exists(text="Settings") # alias of above property. 

# advanced usage
d(text="Settings").exists(timeout=3) # wait Settings appear in 3s, same as .wait(3)
```
* Retrieve the info of the specific UI object
```python
d(text="Settings").info
```

  Below is a possible output:

```python
{ 
  'contentDescription': '',
  'checked': False,
  'scrollable': False,
  'text': 'Settings',
  'packageName': 'com.android.launcher',
  'selected': False,
  'enabled': True,
  'bounds': {
    'top': 385,
    'right': 360,
    'bottom': 585,
    'left': 200
   },
  'className': 'android.widget.TextView',
  'focused': False,
  'focusable': True,
  'clickable': True,
  'chileCount': 0,
  'longClickable': True,
  'visibleBounds': {
    'top': 385,
    'right': 360,
    'bottom': 585,
    'left': 200
  },
  'checkable': False
}
```

* Get/Set/Clear text of an editable field (e.g., EditText widgets)

```python
d(text="Settings").get_text()  # get widget text
d(text="Settings").set_text("My text...")  # set the text
d(text="Settings").clear_text()  # clear the text
```

* Get Widget center point

```python
x, y = d(text="Settings").center()
# x, y = d(text="Settings").center(offset=(0, 0)) # left-top x, y
```

* Take a screenshot of the widget

```python
im = d(text="Settings").screenshot()
im.save("settings.jpg")
```

#### Perform the click action on the selected UI object

* Perform click on the specific object

```python
# click in the center of the specific UI object
d(text="Settings").click()

# wait for an element to appear for at most 10 seconds and then click
d(text="Settings").click(timeout=10)

# click with offset(x_offset, y_offset)
# click_x = x_offset * width + x_left_top
# click_y = y_offset * height + y_left_top
d(text="Settings").click(offset=(0.5, 0.5)) # Default center
d(text="Settings").click(offset=(0, 0)) # click left-top
d(text="Settings").click(offset=(1, 1)) # click right-bottom

# click when exists in 10s, default timeout 0s
clicked = d(text='Skip').click_exists(timeout=10.0)

# click until an element is gone, return bool
is_gone = d(text="Skip").click_gone(maxretry=10, interval=1.0) # maxretry default 10, interval default 1.0
```

* Perform long click on the specific UI object

```python
# long click in the center of the specific UI object
d(text="Settings").long_click()
```

#### Gesture actions for the specific UI object

* Drag the UI object towards another point or another UI object

```python
# notes: drag cannot be used for Android<4.3. 
# drag the UI object to a screen point (x, y), in 0.5 second
d(text="Settings").drag_to(x, y, duration=0.5)
# drag the UI object to (the center position of) another UI object, in 0.25 second
d(text="Settings").drag_to(text="Clock", duration=0.25)
```

* Swipe from the center of the UI object to its edge

  Swipe supports 4 directions:
  - "left"
  - "right"
  - "top"
  - "bottom"
  
```python
d(text="Settings").swipe("right")
d(text="Settings").swipe("left", steps=10)
d(text="Settings").swipe("up", steps=20) # 1 steps is about 5ms, so 20 steps is about 0.1s
d(text="Settings").swipe("down", steps=20)
```

* Two-point gesture from one point to another

```python
d(text="Settings").gesture((sx1, sy1), (sx2, sy2), (ex1, ey1), (ex2, ey2))
```

* Two-point gesture on the specific UI object

  Supports two gestures:
  - `In`, from edge to center
  - `Out`, from center to edge

```python
# notes: pinch cannot be set until Android 4.3. 
# from edge to center. here is "In" not "in"
d(text="Settings").pinch_in(percent=100, steps=10)
# from center to edge
d(text="Settings").pinch_out()
```

* Wait until the specific UI appears or disappears

```python
# wait until the UI object appears
d(text="Settings").wait(timeout=3.0) # return bool
# wait until the UI object gone
d(text="Settings").wait_gone(timeout=1.0)
```

The default timeout is 20s; see **global settings** for more details

* Perform fling on the specific UI object(scrollable)

  Possible properties:
  - `horiz` or `vert`
  - `forward` or `backward` or `toBeginning` or `toEnd`
  
```python
# fling forward(default) vertically(default) 
d(scrollable=True).fling()
# fling forward horizontally
d(scrollable=True).fling.horiz.forward()
# fling backward vertically
d(scrollable=True).fling.vert.backward()
# fling to beginning horizontally
d(scrollable=True).fling.horiz.toBeginning(max_swipes=1000)
# fling to end vertically
d(scrollable=True).fling.toEnd()
```

* Perform scroll on the specific UI object(scrollable)
  Possible properties:
  - `horiz` or `vert`
  - `forward` or `backward` or `toBeginning` or `toEnd`, or `to`

```python
# scroll forward(default) vertically(default)
d(scrollable=True).scroll(steps=10)
# scroll forward horizontally
d(scrollable=True).scroll.horiz.forward(steps=100)
# scroll backward vertically
d(scrollable=True).scroll.vert.backward()
# scroll to beginning horizontally
d(scrollable=True).scroll.horiz.toBeginning(steps=100, max_swipes=1000)
# scroll to end vertically
d(scrollable=True).scroll.toEnd()
# scroll forward vertically until specific UI object appears
d(scrollable=True).scroll.to(text="Security")
```

### WatchContext

The current watch\_context is started with threading and checks every 2 seconds. Currently, there is only one trigger operation, click.

```python
with d.watch_context() as ctx:
    # When the (Download Now or Update Now) and Cancel buttons appear at the same time, click Cancel
    ctx.when("^Download Now|Update Now").when("Cancel").click()
    ctx.when("Agree").click() 
    ctx.when("Confirm").click() # The above three lines of code are executed immediately, and there will be no waiting
    
    ctx.wait_stable() # Turn on pop-up window monitoring and wait for the interface to stabilize (no pop-up window within the two pop-up window inspection cycles means stability) 
    
    # Use call function to trigger function callback
    # call supports two parameters, d and el, regardless of parameter position, and can be passed without parameters. If the parameter variable name is passed, it cannot be wrong
    # eg: When an element matches Midsummer Night, click the return button
    ctx.when("Midsummer Night").call(lambda d: d.press("back")) 
    ctx.when("Confirm").call(lambda el: el.click()) 
    
    # Other operations
    # For convenience, you can also use the default pop-up monitoring logic in the code. 
    
    # The following is the current built-in default logic. 
    # You can add a group at the group owner, add new logic, or directly submit a pr 
    # when("Continue to use").click() 
    # when("Move into control").when("Cancel").click() 
    # when("^Immediately(Download|Update)").when("Cancel").click()
    # when("Agree").click() 
    # when("^(OK|OK)").click()
    
    with d.watch_context(builtin=True) as ctx: # Add on the existing basis 
        ctx.when("@tb:id/jview_view").when('//*[@content-desc="图片"]').click() 
        
        # Other script logic
```

Another way to write

```python
ctx = d.watch_context()
ctx.when("Set").click()
ctx.wait_stable() # Wait for the interface to stop popping up
ctx.close()
```
### Watcher

**It is** recommended to **use WatchContext, which is more concise.**

~~You can register [watchers](http://developer.android.com/tools/help/uiautomator/UiWatcher.html) to perform some actions when a selector does not find a match.~~

Prior to 2.0.0, the [Watcher]((http://developer.android.com/tools/help/uiautomator/UiWatcher.html) method provided by the uiautomator-jar library was used. However, in practice, it was found that once the uiautomator connection failed and was restarted, all watcher configurations were lost, which was definitely unacceptable.

Therefore, the current method uses a thread running in the background (relying on the threading library), then dumps the hierarchy every once in a while, and performs corresponding operations after matching the elements.

Usage Examples

Registration Monitoring

```python
# Common writing method, register anonymous monitoring
 d.watcher.when("Install").click() 

# Register a monitor named ANR. When ANR and Force Close appear, click Force Close 
d.watcher("ANR").when(xpath="ANR").when("Force Close").click() 
# Other callback examples 
d.watcher.when("Grab red envelope").press("back") 
d.watcher.when("//*[@text= 'Out of memory']").call(lambda d: d.shell('am force-stop com.im.qq')) 

# Callback description 
def click_callback(d: u2.Device): 
  d.xpath("OK").click() # Calling in the callback will not trigger the watcher again 

d.xpath("Continue").click() # When using d.xpath to check the element, the watcher will be triggered (currently up to 5 times) 

# Start background monitoring 
d.watcher.start()
```

Monitoring Operations
```python
# Remove ANR monitoring
d.watcher.remove("ANR") # Remove all monitoring
d.watcher.remove() # Start background monitoring

d.watcher.start() 
d.watcher.start(2.0) # Default monitoring interval 2.0s

# Force all monitoring to run
d.watcher.run() 

# Stop monitoring 
d.watcher.stop() 

# Stop and remove all monitoring, often used for initialization
d.watcher.reset()
```

In addition, there are still many documents [uiautomator2/watcher.py](uiautomator2/watcher.py) that are not written. It is recommended to go directly to the source of watcher.py

### Global settings

```python
u2.HTTP_TIMEOUT = 60 # Default value 60s, http default request timeout
```

Most of the other configurations are currently concentrated in `d.settings`, and the configurations may increase or decrease based on later needs.

```python
print(d.settings)

{
    'operation_delay': (0, 0),
    'operation_delay_methods': ['click', 'swipe'],
    'wait_timeout': 20.0
}

# Configure a delay of 0.5s before clicking and a delay of 1s after clicking 
d.settings['operation_delay'] = (.5, 1)

# Modify the method of delay effect
# Double_click and long_click both correspond to click 
d.settings['operation_delay_methods'] = ['click', 'swipe', 'drag', 'press'] 
d.settings['wait_timeout'] = 20.0 # Default control waiting time (native operation, waiting time of xpath plug-in) 

d.settings['max_depth'] = 50 # Default 50, limit the element level returned by dump_hierarchy
```

When setting an expired configuration as the version is upgraded, a Deprecated prompt will be displayed, but no exception will be thrown.

```bash
>>> d.settings['click_before_delay'] = 1  
[W 200514 14:55:59 settings:72] d.settings[click_before_delay] deprecated: Use operation_delay instead
```

**uiautomator recovery mode settings**

If you are careful, you may find that there are actually two APKs installed on your phone, one of which is visible in the foreground (the shared app). 
A package named `com.github.uiautomator.test` is not visible in the background. These two apks are signed with the same certificate. 
The invisible application is actually a test package that contains all the test codes, and the core test service is also started through it. 
However, when running, the system requires the yellow car to be running all the time (it can also run in the background). 

Once the Ofo app is killed, the test service running in the background will also be killed quickly. Even if you don't do anything, the app app is in the background and will be quickly recycled by the system. (I'm hoping for some expert guidance here on how I can do this without relying on the Little Yellow Car app, it feels like it's theoretically possible, but at the moment I won't)

~~There are two ways to make the little yellow car run in the background, one after launching the app and putting it in the background (default). Another way is` to start a background service through` 'am startservice'.~~

~~`You can adjust this behavior `through d.settings["uiautomator\_runtest\_app\_background"] = True True means launching the application, False means starting a service.~~

UiAutomator Timeout Settings (Hidden Methods)

```python
>>> d.jsonrpc.getConfigurator() 
{'actionAcknowledgmentTimeout': 500,
 'keyInjectionDelay': 0,
 'scrollAcknowledgmentTimeout': 200,
 'waitForIdleTimeout': 0,
 'waitForSelectorTimeout': 0}

>>> d.jsonrpc.setConfigurator({"waitForIdleTimeout": 100})
{'actionAcknowledgmentTimeout': 500,
 'keyInjectionDelay': 0,
 'scrollAcknowledgmentTimeout': 200,
 'waitForIdleTimeout': 100,
 'waitForSelectorTimeout': 0}
```

To prevent client program response timeouts, `waitForIdleTimeout` and `waitForSelectorTimeout` have now been changed to 0`

Refs: [Google uiautomator Configurator](https://developer.android.com/reference/android/support/test/uiautomator/Configurator)
### Input method
This method is typically used for input when the UI controls/elements are unknown.
```python
# Text Input Methods  # Basic input through clipboard paste mechanism (current implementation) 
d.send_keys("你好123abcEFG")  # Input text via clipboard  
# Input with clearing previous content 
d.send_keys("你好123abcEFG", clear=True)  # Clear field first, then input  

# Clear text field 
d.clear_text()  # Clear all content from input field

d.send_action()  # Automatic action execution (Added in version 3.1)  
# Automatically execute enter/search based on input field type  # Specify input method action d.send_action("search")  # Explicitly specify action type  # Supported actions: # - go # - search # - send # - next # - done # - previous 
```

```python
print(d.current_ime()) # Get the current input method ID
```

> More references: [IME_ACTION_CODE](https://developer.android.com/reference/android/view/inputmethod/EditorInfo)

### Toast

```python
print(d.last_toast) # get last toast, if not toast return None
d.clear_toast()
```

> Fixed in version 3.2.0
### XPath
Java uiautoamtor does not support XPath by default, so this is an extended function. The speed is not that fast.

For example: the content of one of the nodes

```xml
<android.widget.TextView
  index="2"
  text="05:19"
  resource-id="com.netease.cloudmusic:id/qf"
  package="com.netease.cloudmusic"
  content-desc=""
  checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false"
  scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true"
  bounds="[957,1602][1020,1636]" />
```

xpath positioning and usage

Some attribute names have been modified and need attention

```
description -> content-desc
resourceId -> resource-id
```

Common usage

```python
# wait exists 10s
d.xpath("//android.widget.TextView").wait(10.0)
# find and click
d.xpath("//*[@content-desc='分享']").click()# check exists

if d.xpath("//android.widget.TextView[contains(@text, 'Se')]").exists:
    print("exists")# get all text-view text, attrib and center point
  
for elem in d.xpath("//android.widget.TextView").all():    
    print("Text:", elem.text)    
    # Dictionary eg:     
    # {'index': '1', 'text': '999+', 'resource-id': 'com.netease.cloudmusic:id/qb', 'package': 'com.netease.cloudmusic', 'content-desc': '', 'checkable': 'false', 'checked': 'false', 'clickable': 'false', 'enabled': 'true', 'focusable': 'false', 'focused': 'false','scrollable': 'false', 'long-clickable': 'false', 'password': 'false', 'selected': 'false', 'visible-to-user': 'true', 'bounds': '[661,1444][718,1478]'} 
    print("Attrib:", elem.attrib)
    # Coordinate eg: (100, 200)
    print("Position:", elem.center())
```

Click [to view other](./XPATH.md) common uses of XPath

### Screenrecord (Deprecated)
Video recording (deprecated), use [scrcpy instead](https://github.com/Genymobile/scrcpy)!

The screenrecord command that comes with the mobile phone is not used here. The method of synthesizing videos by obtaining mobile phone pictures is used, so some other dependencies need to be installed, such as imageio, imageio-ffmpeg, numpy, etc. Because some dependencies are relatively large, it is recommended to use mirror installation.

Just run the following command.

```bash
pip3 install -U "uiautomator2[image]" -i https://pypi.doubanio.com/simple
```

Usage

```python
d.screenrecord('output.mp4')

time.sleep(10)# or do something else

d.screenrecord.stop() # 停止录制后，output.mp4文件才能打开
```

You can also specify the fps when recording (currently 20). This value is lower than the speed at which minicap outputs images. It feels good enough and I don't recommend changing it.

# Enable uiautomator2 logger

```python
from uiautomator2 import enable_pretty_logging
enable_pretty_logging()
```

Or

```python
logger = logging.getLogger("uiautomator2")
# setup logger
```

## Stop UiAutomator

When the Python program exits, UiAutomation exits. 
However, you can also stop the service through the interface method

```python
d.stop_uiautomator()
```

## Differences between Google UiAutomator 2.0 and 1.x
https://www.cnblogs.com/insist8089/p/6898181.html

- New interfaces: UiObject2, Until, By, BySelector
- Introduced by: com.android.uiautomator.core.\* Introduced by: com.android.uiautomator.core.\* Introduced by: com.android.uiautomator.core.\* Deprecated in 2.0. 改为android.support.test.uiautomator
- Build system: Maven and/or Ant (1.x); Gradle (2.0)
- The format of the generated test package: from zip/jar (1.x) to apk (2.0)
- Run UIAutomator tests with 
  adb commands in the local environment. The differences in startup methods are: 
  adb shell uiautomator runtest UiTest.jar -c package.name.ClassName (1.x) adb shell am instrument -e class com
  .example.app.MyTestcom.example.app.test/android.support.test.runner.AndroidJUnitRunner (2.0)
- Can I use Android services and interfaces? 1.x~No; 2.0~Yes.
- og output? Use System.out.print output stream to echo to the execution end (1.x); output to Logcat (2.0)
- implement? Test cases do not need to inherit from any parent class, the method name is not limited, and use annotations (2.0); need to inherit UiAutomatorTestCase, and the test method needs to start with test (1.x)
## Dependent Projects
- uiautomator jsonrpc server [openatx/android-uiautomator-server](https://github.com/openatx/android-uiautomator-server/)
- ~~uiautomator daemon [openatx/atx-agent](https://github.com/openatx/atx-agent)~~
# Contributors
- codeskyblue ([@codeskyblue][])
- Xiaocong He ([@xiaocong][])
- Yuanyuan Zou ([@yuanyuan][])
- Qian Jin ([@QianJin2013][])
- Xu Jingjie ([@xiscoxu][])
- Xia Mingyuan ([@mingyuan-xia][])
- Artem Iglikov, Google Inc. ([@artikz][])

[@codeskyblue]: https://github.com/codeskyblue
[@xiaocong]: https://github.com/xiaocong
[@yuanyuan]: https://github.com/yuanyuanzou
[@QianJin2013]: https://github.com/QianJin2013
[@xiscoxu]: https://github.com/xiscoxu
[@mingyuan-xia]: https://github.com/mingyuan-xia
[@artikz]: https://github.com/artikz

Other [contributors](../../graphs/contributors)
## Other outstanding projects
- https://github.com/atinfo/awesome-test-automation A collection of all excellent test frameworks, covering everything
- [google/mobly is](https://github.com/google/mobly) Google's internal testing framework. Although I don't understand it very well, it seems to be very useful.
- https://github.com/zhangzhao4444/Maxim Monkey based on Uiautomator
- http://www.sikulix.com/ An automated testing framework based on image recognition, very old
- http://airtest.netease.com/ The predecessor of this project was later taken over and further optimized by the NetEase Guangzhou team. Implementation has a nice IDE

The ranking is in order, welcome to add
# LICENSE
[MIT](LICENSE)