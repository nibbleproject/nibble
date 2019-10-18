# nibble

[![CircleCI](https://circleci.com/gh/nibbleproject/nibble/tree/master.svg?style=svg)](https://circleci.com/gh/nibbleproject/nibble/tree/master)
[![Coveralls](https://img.shields.io/coveralls/nibbleproject/nibble.svg)](https://coveralls.io/r/nibbleproject/nibble)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/nibbleproject/nibble.svg)](https://scrutinizer-ci.com/g/nibbleproject/nibble/)
[![Join the chat at https://gitter.im/nibbleproject/nibble](https://badges.gitter.im/nibbleproject/nibble.svg)](https://gitter.im/nibbleproject/nibble)

A webcomics platform that tries its best to be easy to get going with.

## Mission

Publishing a webcomic can be frustrating, especially for the technology-averse. Many publishing platforms are built for blogs, leading to awkward translations between the blog and webcomic models that can lead to confusion and compromise.

Nibble aims to be a friendly platform tailor-made for webcomics with the option to self-host.

The project's core principles are:

- Be simple
- Be accessibile
- Be inclusive
- Support creators
- Have fun
- Open source everything
- NO ADS

## Roadmap

Here's a totally arbitrary set of goals I just made up.

### Stage 1: Prototype

A prototype will be built that includes the following features:

- Comics!
- Customizable comic appearance
- Custom domains per comic
- Scheduled publishing
- Heroku and Docker deployment support

This isn't a complete list, but it includes what we consider the core features needed for public comics.
Once the core features are implemented, we'll move on to the Alpha phase.

### Stage 2: Alpha

During the Alpha phase, authors will be encouraged to test the platform by publishing real comics on both an
invite-only hosted instance and self-hosted instances. We'll collect as much feedback as possible and work out
any major bugs, scaling issues, and other problems before launching an officially supported release.

If this project has any other contributors at that time, we'll work out a set of contributor guidelines and a release
schedule.

Depending on the scale of the project, this would be the point at which we'd come up with a funding model or some
other way to support development. If that happens, the aim will be to support *all* contributors, not just the core
group.

### Stage 3: Release

Once the kinks are worked out, Nibble will be ready for general availability! We'll open up registration to the
hosted instance, provide some sort of support to self-hosters, and have a huge Internet party.

We could call this stage "Beta", but everything on the Internet is always in Beta.

## Development

### Installing dependencies

Nibble uses [pipenv](https://docs.pipenv.org) to manage dependencies. To get started, install pipenv:

```bash
$ pip install pipenv
```

Then, install dependencies and create a virtualenv all at once:

```bash
$ pipenv install --dev
```

To drop into a shell inside the virtualenv:

```bash
$ pipenv shell
```

Learn more about pipenv by [reading the docs](https://docs.pipenv.org).

## Deploying

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### Docker

See [Running with Docker](docker/README.md).
