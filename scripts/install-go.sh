#!/usr/bin/env bash

#------------------------------------------------------------------------------
# @file
# This file installs go, so that go modules can be used.
#------------------------------------------------------------------------------

main() {

  GO_VERSION=1.25.4

  export TZ=Europe/Zurich

  # Install Go
  echo "Installing Go ${GO_VERSION}..."
  mkdir -p "${HOME}/.local"
  curl -sLJO "https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz"
  tar -C "${HOME}/.local" -xf "go${GO_VERSION}.linux-amd64.tar.gz"
  rm "go${GO_VERSION}.linux-amd64.tar.gz"
  export PATH="${HOME}/.local/go/bin:${PATH}"
  go version
}

set -euo pipefail
main "$@"
