# rotdis

This is a Python app for rotating the display in Windows 10.

## Requirements

The following dependencies must already be installed on your system:

| Dependency                                  | Version |
| ------------------------------------------- | ------- |
| [python](https://www.python.org/downloads/) | ^3.12   |
| [pipx](https://pipx.pypa.io/stable/)        | ^1.6    |

This app was written on and for Windows 10 (x64). It may work on other operating systems but it is
not officially supported.

## Setup

Install the app using `pipx`, e.g. directly from GitHub using SSH:

```
$ pipx install git+ssh://git@github.com/own-neufeldm/rotdis.git

  installed package rotdis 1.0.1, installed using Python 3.12.5
  These apps are now globally available
    - rotdis.exe
done! ✨ 🌟 ✨
```

You can now run the app using `rotdis`.

## Usage

Upon running `rotdis`, the app will rotate your display depending on the current orientation:

| Orientation before | Orientation after |
| ------------------ | ----------------- |
| Landscape (0)      | Portrait (90)     |
| Portrait (90)      | Landscape (0)     |

Other orientations are not supported at the moment.
