BASEDIR="$(cd "$(dirname "$0")"; pwd)"
source "$BASEDIR"/venv/bin/activate && python "$BASEDIR"/khallas_cli.py --gui=true
