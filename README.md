# django-MaryaNutri
Django e-commerce website of [MaryaNutri](https://www.maryanutri.com)

## Local setup instructions (for superior linux users)

```bash
# Clone repository
git clone git@github.com:robsyc/django-MaryaPorr.git
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
  - [ ] Logo
    - [ ] Calabash-like with colors
    - [ ] Square, wide, favicon
  - [ ] Hero section (See: [page](https://www.italiancricketfarm.com/)) with square logo
  - [x] Infinite looping image carousel
  - [ ]  (check out powerpoint)
    - [x] 1. Malnutrition stats (of children) in the world (from WHO)
    - [ ] 2. Visual comparison/ecological footprint of insect vs. chicken vs. cow (e.g. nutrients, water, land, GHG emissions)
    - [ ] 3. Relief / food aid stats (how much money is spent)
- [x] About page: team, story, documentary
- [ ] Favicon
- [ ] Footer
  - [ ] Sign up for newsletter form
  - [ ] Body bg nav-green to footer-grey
- [ ] List view (4-6 products)
  - [ ] Images local static instead of S3
  - [ ] Cart ~ session
- [ ] Detail view (product) with technical info
  - [ ] Breadcrumb
  - [ ] Redirect to Stripe directly
  - [ ] Basket
- [x] Hide Stripe API details (and other env variables)
- [x] Setup Cloudflare domain
- [x] Host on [Render](https://docs.render.com/deploy-django) or Vercel?
- [ ] Complete Stripe profile w/ company & bank details
- [ ] Multi-language support (e.g. for Swahili)
