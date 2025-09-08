# iam-lib change log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## (0.0.18) 2025-09-07
### Added/Changed/Fixed
- Extend token decoding and validation in Token class

## (0.0.17) 2025-09-07
### Added/Changed/Fixed
- Add EDI token refresh API method

## (0.0.16) 2025-08-18
### Added/Changed/Fixed
- Align create_token with IAM API to use authentication key

## (0.0.15) 2025-08-15
### Added/Changed/Fixed
- Add group client API
- Change all API calls to return a response object

## (0.0.14) 2025-07-10
### Added/Changed/Fixed
- Change "pasta_token" to "edi-token"

## (0.0.12) 2025-07-06
### Added/Changed/Fixed
- Change Permission enum to type Flag and add permission map attribute
- Update rule API class to use flag-type Permission

## (0.0.11) 2025-07-02
### Added/Changed/Fixed
- Add HTTP requests retry decorator for failed connections

## (0.0.10) 2025-06-30
### Added/Changed/Fixed
- Add HTTP requests timeout option for all client calls (defaults to 10 seconds)

## (0.0.9) 2025-06-23
### Added/Changed/Fixed
- Added permission enumerations
- Refactored method signatures to align with IAM API

## (0.0.8) 2025-06-19
### Added/Changed/Fixed
- Disregard port number associated with the host name during validation

## (0.0.7) 2025-06-18
### Added/Changed/Fixed
- Support local trust store for SSL certificate verification

## (0.0.6) 2025-06-01
### Added/Changed/Fixed
- Add EDI Token Client API and unit tests
- Refactor "parameters" to "form_params" to align with Python requests package
- Add configuration module to tests

## (0.0.5) 2025-05-29
### Added/Changed/Fixed
- Update methods to rely on cookie token to identify principals

## (0.0.4) 2025-05-26
### Added/Changed/Fixed
- Use requests Response object in place of the IAM Response class 

## (0.0.3) 2025-05-22
### Added/Changed/Fixed
- Add profile API client

## (0.0.2) 2025-05-20
### Added/Changed/Fixed
- Refactor API module functions to subclasses of the Client class
- Add support for requests `params` for GET

## (0.0.1) 2025-05-17
### Added/Changed/Fixed
- First release with complete module test coverage, albeit limited

## (0.0.0) 2025-05-04
### Added/Changed/Fixed
- Initial build
