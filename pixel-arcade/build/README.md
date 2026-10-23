# Local fork build record

Branch: pixel-local. Application display name: Zed Pixel.

The official Zed application remains installed until the fork passes validation.
The Xcode SDK is selected per command using DEVELOPER_DIR; the system-wide developer directory is not changed.
Rust toolchain: 1.98.1. CMake installed via Homebrew.

First regression test: client::tests::test_local_build_never_starts_zed_authentication.
It exercises production authentication with a trap callback and checks that the callback is never invoked and status stays SignedOut.

Brand assets are in ../branding. Their source is a 32×32 grid SVG; PNG sizes and macOS ICNS were generated from that grid.
