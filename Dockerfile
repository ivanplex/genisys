# https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
FROM python:3.7-slim

# Install packages needed to run your application (not build deps):
#   mime-support -- for mime types when serving static files
#   postgresql-client -- for running database commands
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN set -ex \
    && RUN_DEPS=" \
        libpcre3 \
        mime-support \
        postgresql-client \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

ADD ./requirements/prod.txt	/genisys/requirements/prod.txt

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step.
# Correct the path to your production requirements file, if needed.
RUN set -ex \
    && BUILD_DEPS=" \
        build-essential \
        libpcre3-dev \
        libpq-dev \
    " \
    && apt-get update && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip install -U pip \
    && pip install --no-cache-dir -r /genisys/requirements/prod.txt \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /genisys
COPY . /genisys/

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
#CMD ["gunicorn", "genisys.wsgi", "-b", ":8080"]