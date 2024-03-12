# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.2] - 2024-03-10
### Fixed
- "tox.tox_env.errors.Recreate: requirements removed" if requirements change by
  recreating the tox testenv if a Recreate error is encountered ([#2]).

### Changed
- Simplified test in `example/` to use src-layout, avoiding `sys.path`
  manipulation and using `importlib` instead of `setuptools` to check if the
  package is installed.

[#2]: https://github.com/sclabs/tox-extras/issues/2

## [0.0.1] - 2022-04-19
Initial release.

[0.0.2]: https://github.com/sclabs/tox-extras/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/sclabs/tox-extras/releases/tag/v0.0.1
