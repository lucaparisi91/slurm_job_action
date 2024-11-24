module load cray-python/3.10.10
python -m venv $GITHUB_ACTION_PATH/runner_env
source $GITHUB_ACTION_PATH/runner_env/bin/activate
pip install --upgrade pip
pip install pyyaml
