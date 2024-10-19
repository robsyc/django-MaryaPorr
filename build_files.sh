echo "BUILD START"

python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
pwd
ls

echo "BUILD END"
