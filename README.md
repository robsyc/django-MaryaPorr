# django-MaryaPorr
Django e-commerce website of [MaryaPorr](https://www.maryaporr.com)

## Local setup instructions (for superior linux users)

```bash
# Clone repository
git clone https://github.com/robsyc/django-MaryaPorr.git
cd django-MaryaPorr

# Create and setup virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Create and setup .env variables
cp .env.example .env

# Setup Django & DB
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Kill default Django port FYI
fuser -k 8000/tcp
```

## To-do
- [ ] Landing page
- [ ] About page
- [ ] List view (4-6 products)
- [ ] Detail view (product) with technical info and redirect to buy on Stripe
- [ ] Hide Stripe API details
- [x] Setup Cloudflare domain
- [ ] Host on [Render](https://docs.render.com/deploy-django) or Vercel?
- [ ] Complete Stripe profile w/ company & bank details
- [ ] Multi-language support (e.g. for Swahili)
