# Changelog

## 1.1.1 (2025-11-12)

Full Changelog: [v1.1.0...v1.1.1](https://github.com/fakerybakery/hfapi/compare/v1.1.0...v1.1.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([20b76f9](https://github.com/fakerybakery/hfapi/commit/20b76f9521faad8dbfe6d062b7d178584e804529))
* compat with Python 3.14 ([f614400](https://github.com/fakerybakery/hfapi/commit/f6144002fff7364f79173ff4f29589777af84983))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([5d8a1df](https://github.com/fakerybakery/hfapi/commit/5d8a1df29d66301f86a5a9bb9691f9801c5115af))
* do not set headers with default to omit ([68d2133](https://github.com/fakerybakery/hfapi/commit/68d2133de760f0fa4ef7554589cdf22be6bcde07))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([cc6e7c1](https://github.com/fakerybakery/hfapi/commit/cc6e7c107c2cfeacc8f95729392edced88fa368b))
* do not install brew dependencies in ./scripts/bootstrap by default ([52c71ab](https://github.com/fakerybakery/hfapi/commit/52c71ab6142322177b2a5454d93cd7a2047eae41))
* **internal/tests:** avoid race condition with implicit client cleanup ([06f50fe](https://github.com/fakerybakery/hfapi/commit/06f50fe4d4d6a9841c8eb35bdf8fef13a319a278))
* **internal:** detect missing future annotations with ruff ([5205295](https://github.com/fakerybakery/hfapi/commit/5205295b584f86ee845cf0cd027bd5b93c1f80da))
* **internal:** grammar fix (it's -&gt; its) ([911dbd8](https://github.com/fakerybakery/hfapi/commit/911dbd82e26ec1d3a2e594778883f6c176e2b398))
* **internal:** update pydantic dependency ([8a07add](https://github.com/fakerybakery/hfapi/commit/8a07adda6881a0adb2175ee9c6a400bbecb94cfa))
* **package:** drop Python 3.8 support ([6a66393](https://github.com/fakerybakery/hfapi/commit/6a66393b18813e4ed162ef15e999474597c1560b))
* **types:** change optional parameter type from NotGiven to Omit ([d937e6e](https://github.com/fakerybakery/hfapi/commit/d937e6e9e05036e095b6fd2c5a017cfa6c77296a))

## 1.1.0 (2025-09-16)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/fakerybakery/hfapi/compare/v1.0.0...v1.1.0)

### Features

* **api:** update package name to pyhfapi ([a00af0b](https://github.com/fakerybakery/hfapi/commit/a00af0bdfb492f9dc8a5e378a10b22c8978f9353))

## 1.0.0 (2025-09-16)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/fakerybakery/hfapi/compare/v0.0.1...v1.0.0)

### Features

* **api:** manual updates ([f545fbc](https://github.com/fakerybakery/hfapi/commit/f545fbc3e9e8ef2c11dc191f6c771b1c584661d9))


### Chores

* update SDK settings ([06c0775](https://github.com/fakerybakery/hfapi/commit/06c0775ed42e67eb9ff058afa5f846b30c3d6d5b))
* update SDK settings ([ee7df49](https://github.com/fakerybakery/hfapi/commit/ee7df4975332289dc3265769d635babbdd3602cb))
