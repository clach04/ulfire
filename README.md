# fauxhue / Ulfire

Home page https://github.com/clach04/ulfire
a fork of https://github.com/mjg59/ulfire

fauxhue / Ulfire is a simple Python 2 (py3 TODO) application that detects and controls LIFX and
Belkin WeMo Link LED bulbs by exporting a sufficient subset of the Philips
Hue API to convince the Amazon Echo that it's speaking to a real Hue.

In other words, it lets you use an Amazon Echo to voice control your LIFX or
WeMo Link lights.

Both LIFX and WeMo support is optional.

## Problems

  * no Python 3 (byte) support
  * does not respond to discovery requests from miranda nor https://github.com/Overboard/discoverhue.git
  * does not respond to json payload (from cURL)
  * does not respond to config url

#### cURL Philips Hue samples

    echo IP needs to include colon port if NOT using port 80
    export USERNAME=nouser
    export IP=127.0.0.0:80
    export LIGHTNUM=1  # pick the first one, what ever it maybe
    curl -v http://${IP}/description.xml
    curl -v http://${IP}/api/${USERNAME}/lights
    curl -v http://${IP}/api/${USERNAME}/config

    curl -v http://${IP}/api/${USERNAME}/lights/${LIGHTNUM}
    curl -s -H "Accept: application/json" -X PUT --data "{\"on\": true}"  http://${IP}/api/${USERNAME}/lights/${LIGHTNUM}/state
    curl -s -H "Accept: application/json" -X PUT --data "{\"on\": false}" http://${IP}/api/${USERNAME}/lights/${LIGHTNUM}/state



Requirements
------------

You'll need a machine on your local network to run this on. It needs to be
on the same network as the Echo and your lights. It probably needs to be
vaguely Unixish - I've only tested this on Linux, but it almost certainly
runs fine on BSDs and it's probably fine on MacOS X. I have no idea about
Windows, but I wouldn't be optimistic. You **may** want to install the
LazyLights and Ouimeaux Python modules:

    pip install git+https://github.com/mpapi/lazylights@2.0
    pip install git+https://github.com/iancmcc/ouimeaux

and then just run ulfire.py. It'll automatically detect your lights (note
that the lights must already be configured and named with the vendor
apps). Once that's done, just ask your Echo to detect connected devices. It
should find all your bulbs. Create any groups you want to via the Echo
settings UI, and then you should be able to turn your lights on and off and
dim them.

Thanks
------

This code is derived from Fauxmo (https://github.com/makermusings/fauxmo)
