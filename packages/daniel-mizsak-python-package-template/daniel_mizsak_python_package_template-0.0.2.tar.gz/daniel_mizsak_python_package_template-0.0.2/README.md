## <div align="center"> 🐍 python-package-template</div>

<div align="center">
<a href="https://github.com/daniel-mizsak/python-package-template/actions/workflows/ci.yml" target="_blank"><img src="https://github.com/daniel-mizsak/python-package-template/actions/workflows/ci.yml/badge.svg" alt="build status"></a>
<a href="https://results.pre-commit.ci/latest/github/daniel-mizsak/python-package-template/main" target="_blank"><img src="https://results.pre-commit.ci/badge/github/daniel-mizsak/python-package-template/main.svg" alt="pre-commit.ci status"></a>
<a href='https://daniel-mizsak-python-package-template.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/daniel-mizsak-python-package-template/badge/?version=latest' alt='docs status' /></a>
<a href="ttps://img.shields.io/github/license/daniel-mizsak/python-package-template" target="_blank"><img src="https://img.shields.io/github/license/daniel-mizsak/python-package-template" alt="license"></a>
</div>


## Overview
A GitHub template with my python package configurations.


## Getting started


## Setting on a GitHub repository
- `Code` -> `About` -> `Settings` -> Disable `Packages` and `Deployments`
- `Settings` -> `Features` -> Only enable `Issues`
- `Settings` -> `Pull Reqests` -> Only disable `Always suggest updating pull request branches` and `Allow auto-merge`
- `Settings` -> `Branches` -> `Add rule` -> `main` -> Protect matching branches -> Enable `Require pull request reviews before merging` and `Dismiss stale pull request approvals when new commits are pushed`
- `Require status checks to pass before merging` -> `pre-commit.ci - pr` and `tox / tox`

## Setup PyPi trusted publishing
