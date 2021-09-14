# Getting Started with Python

So you want to learn computer science? Great! Welcome!

There are lots of computer languages to use to learn computer science, but one of them sticks out as probably the best to start with, and that is Python. Here is python's logo:

![python](assets/python.png)

Python is used by Google, researchers at major universities, and companies such as Uber, Instagram, Spotify, Netflix, and [many more](https://stackshare.io/python).

By the end of this chapter you will be able to:

1. Open and use your computer's terminal.
1. Install Homebrew, a package manager for installing programs in your computer.
1. Install Python3 to get started with Python.

# The Terminal, Command Line Interface (CLI)

**You will need a Mac computer to complete this tutorial.**

We'll be installing python using your computers Terminal, or Command Line Interface (CLI), or simply the command line. The CLI is just a text-based interface for using your computer. You can create and copy and paste files, you can open programs, you can even install and uninstall programs all from your command line.

Open your command line by using Spotlight, so hit `Command` + `Spacebar` to open your Spotlight, then type "Terminal" and hit enter.

Your terminal will open. It's kinda ugly, so we're going to make it pretty first.

Go to your settings of your terminal by hitting `Command` + `,` and under the Profiles tab, select the "Pro" style configuration and click "Default". Now close and reopen the Terminal.

Looking sweet :D

# Xcode Tools

First we need some extra tools published by Apple to transform your computer from a normal, regular non-developer computer, into a suped-up engineer's computer!

Let's do that by pasting this command into your terminal (**NOTE: don't include the `$`** — that just means you should run this in the command line):

```bash
$ xcode-select --install
```

> What did we just do? We installed the [Xcode Command Line Tools](https://developer.apple.com/library/archive/technotes/tn2339/_index.html) package. This package gives you all the tools you'll need to do development in the terminal!

Once your xcode commandline tools are installed, move onto the next step. Installing Homebrew.

# Homebrew

If we want to install tools and applications using the terminal, the best program to use is [Homebrew](https://brew.sh/).

If you don't already have Homebrew, install it by following the instructions under `Install Homebrew` on the [Homebrew website](https://brew.sh/)

This will install homebrew into your computer so now we can use it to install Python.

# Installing Python3

We will be using the most advanced version of python there is which as of writing this is Python 3.

To install it on your computer, use homebrew in, you guessed it, the command line terminal.

```bash
$ brew install python3
```

Now you can check if the installation went well by asking for python3's version:

```bash
$ python3 --version
```

If you see `Python 3.7.3` or something similar, then it is installed!

On to the next chapter!

# In Review: You Can ...

1. Open and use your computer's terminal.
1. Install Homebrew, a package manager for installing programs in your computer.
1. Install Python3 to get started with Python.

# Next Steps

Onward! Click [here](../P01-Flash-Cards/content.md) to move onto the next section about making a flash card tester.
