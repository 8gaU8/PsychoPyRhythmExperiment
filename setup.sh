#! /bin/bash
set -euxoC pipefail
cd "$(dirname "$0")"

err() {
  echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $*" >&2
}

export __CFBundleIdentifier="org.opensciencetools.psychopy"
export PATH="$PATH:/Applications/PsychoPy.app/Contents/Resources/git-core"
export _PY2APP_LAUNCHED_="1"
export PYTHONDONTWRITEBYTECODE="1"
export PYTHONUNBUFFERED="1"
export EXECUTABLEPATH="/Applications/PsychoPy.app/Contents/MacOS/PsychoPy"
export RESOURCEPATH="/Applications/PsychoPy.app/Contents/Resources"
export PYTHONPATH="/Applications/PsychoPy.app/Contents/Resources:./pkgs"
export ARGVZERO="/Applications/PsychoPy.app/Contents/MacOS/PsychoPy"
export PYTHONHOME="/Applications/PsychoPy.app/Contents/Resources"
export SSL_CERT_FILE="/Applications/PsychoPy.app/Contents/Resources/openssl.ca/no-such-file"
export SSL_CERT_DIR="/Applications/PsychoPy.app/Contents/Resources/openssl.ca/no-such-file"
export TCL_LIBRARY="/Applications/PsychoPy.app/Contents/Resources/lib/tcl8"
export TK_LIBRARY="/Applications/PsychoPy.app/Contents/Resources/lib/tk8.6"
export GIT_PYTHON_GIT_EXECUTABLE="/Applications/PsychoPy.app/Contents/Resources/git-core/git"
export LD_LIBRARY_PATH="/Applications/PsychoPy.app/Contents/Resources:/Applications/PsychoPy.app/Contents/Resources/lib:/Applications/PsychoPy.app/Contents/Resources/lib"

./scripts/pip_install -r ./requirements.txt

