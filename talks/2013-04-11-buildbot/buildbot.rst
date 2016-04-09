
========
Buildbot
========

:Author: Martin Geisler martin@geisler.net
:Date: 2013-04-11

Continuous Integration, the Python Way

Zurich Python User Group


Introduction
============

* Continuous integration (CI) server written in Python

* Open source --- 10 year anniversary on April 29th!

* Well documented on http://buildbot.net/

* Used by Python, WebKit, Chromium, ...

* How many of you use a CI system?


Terminology
===========

* Continuous Integration: running *builds* automatically on commit

* Build: sequence of *build steps*

* Build step: command such as ``make`` or ``make test``

* Build master: schedules *builds* on *build slaves*

* Build slaves: execute the *builds*


Architecture
============

Buildbot uses a client/server architecture:

* Server: the *build master* schedules builds on build slaves

  - monitors version control system to know when to start a build

  - displays status information in web interface

* Clients: one or more *build slaves* execute the builds

  - test different architectures with slaves on Linux, Mac, Windows...

  - run multiple slaves for better performance


Security
========

Ports open on build master:

* port for web interface

* port for slave communication

Ports open on build slaves: none


Installation
============

Buildbot is packaged for many Linux distributions

Can be installed with Pip:

* On the build master::

    $ pip install buildbot

* On your build slaves::

    $ pip install buildbot-slave


Setup
=====

You create a build master with::

  $ buildbot create-master DIR

Build slaves are created with::

  $ buildslave create-slave DIR HOST:PORT SLAVENAME PASSWORD


Minimal Configuration File
==========================

* Configure project title, URL, ...

* Configure build slaves

* Create a build factory:

  - Add source checkout step

  - Add a shell command step

* Create a builder using the build factory and slaves

* Create a scheduler using the builder

* Create a change source


Dealini's Configuration File
============================

* Two applications: dealini website and mobile app

* Three branches: default, beta, and game

* Two builders: quick and full (which depends on quick)

* Uses the power of Python to generate the configuration

* Uses custom build steps to parse command output


Conclusion
==========

* CI helps you avoid mistakes by ensuring your tests are run

* Buildbot gives you a "CI framework"

* Very flexible and easy to adapt


..  LocalWords:  Buildbot buildbot Django buildslave
