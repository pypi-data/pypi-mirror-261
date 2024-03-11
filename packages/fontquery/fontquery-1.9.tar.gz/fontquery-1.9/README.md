# Fontquery
[![pip version badge](https://img.shields.io/pypi/v/fontquery)](https://pypi.org/project/fontquery/)
[![tag badge](https://img.shields.io/github/v/tag/fedora-i18n/fontquery)](https://github.com/fedora-i18n/fontquery/tags)
[![license badge](https://img.shields.io/github/license/fedora-i18n/fontquery)](./LICENSE)

fontquery is a tool to query fonts in the certain Fedora release.

## How to install

``` shell
$ pip3 install fontquery
```

Or in Fedora,

``` shell
# dnf install fontquery
```

## How to install from git

``` shell
$ pip3 install --user build wheel
$ python3 -m build
$ pip3 install --user dist/fontquery*.whl
```

Or in Fedora,

``` shell
# dnf install python3-build python3-wheel
$ python3 -m build
$ pip3 install --user dist/fontquery*.whl
```

## Usage

```
usage: fontquery [-h] [-r RELEASE] [-l LANG] [-m {fcmatch,fclist,json}] [-t {comps,langpacks,both,all}] [-v]
                 [args ...]

Query fonts

positional arguments:
  args                  Queries (default: None)

options:
  -h, --help            show this help message and exit
  -C, --clean-cache     Clean caches before processing (default: False)
  --disable-cache       Enforce processing everything even if not updating (default: False)
  -r RELEASE, --release RELEASE
                        Release number such as "rawhide" and "39". "local" to query from current environment
                        instead of images (default: local)
  -l LANG, --lang LANG  Language list to dump fonts data into JSON (default: None)
  -m {fcmatch,fclist,json}, --mode {fcmatch,fclist,json}
                        Action to perform for query (default: fcmatch)
  -t {minimal,extra,all}, --target {minimal,extra,all}
                        Query fonts from (default: minimal)
  -v, --verbose         Show more detailed logs (default: 0)
  -V, --version         Show version (default: False)
```

To query sans-serif for Hindi on Fedora 36,

``` shell
$ fontquery -r 36 sans-serif:lang=hi
Lohit-Devanagari.ttf: "Lohit Devanagari" "Regular"
```

To generate JSON from langpacks installed environment:

``` shell
$ fontquery -m json -t langpacks
...
```

To generate html table:

``` shell
$ fontquery -m json -t langpacks | fq2html -o langpacks.html -
```

To check difference between local and reference:

``` shell
$ fontquery-diff -R text rawhide local
```

## For developers

Before committing something into git repository, you may want to do:

``` shell
$ git config core.hooksPath hooks
```

to make sure our hook scripts works.
