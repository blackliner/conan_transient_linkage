#!/bin/bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

conan export "${SCRIPT_DIR}/lib_a"
conan export "${SCRIPT_DIR}/lib_b"
conan export "${SCRIPT_DIR}/lib_c"

conan create "${SCRIPT_DIR}/lib_a" -b missing
conan create "${SCRIPT_DIR}/lib_a" -b missing -o *:shared=True
