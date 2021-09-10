#!/bin/bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

conan create "${SCRIPT_DIR}/lib_c"
conan create "${SCRIPT_DIR}/lib_b"
conan create "${SCRIPT_DIR}/lib_a"

conan create "${SCRIPT_DIR}/lib_c" -o *:shared=True
conan create "${SCRIPT_DIR}/lib_b" -o *:shared=True
conan create "${SCRIPT_DIR}/lib_a" -o *:shared=True
