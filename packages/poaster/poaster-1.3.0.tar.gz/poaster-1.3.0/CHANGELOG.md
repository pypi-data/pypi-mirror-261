# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.3.0 - 2024-03-08

### Added

- Add initial web application.
- Add support for dotenv in pydantic settings.

### Changed

- Move service commands into a class to simplify API.
- Organize cli commands by domain.

### Fixed

- Fetch the secret key from settings not environment.

## 1.2.0 - 2024-03-05

### Added

- Make log level configurable in app settings.
- Add `post_versions` table for tracking post history.
- Expose ability to update and delete posts from JSON API.

## 1.1.0 - 2024-02-13

### Added

- Add JSON API endpoints for handling bulletin posts.

### Fixed

- Constrain the value length of input credentials.

## 1.0.0 - 2024-02-12

### Added

- Add CLI for user management and running the application.
- Add JSON API endpoints for authenticating users with JWT.
