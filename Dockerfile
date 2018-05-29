FROM python:3 as python-base
MAINTAINER Ryan Lopopolo <rjl@hyperbo.la>

COPY Pipfile Pipfile
copy Pipfile.lock Pipfile.lock

RUN pip install pipenv && \
    pipenv install --system --deploy && \
    rm -rf /root/.cache Pipfile Pipfile.lock

COPY hyperbola hyperbola
COPY MANIFEST.in .
COPY README.md .
COPY setup.py .
COPY setup.cfg .

RUN env PBR_VERSION=0.134.0 \
        SKIP_GIT_SDIST=1 \
        SKIP_GENERATE_AUTHORS=1 \
        SKIP_WRITE_GIT_CHANGELOG=1 \
        python setup.py install
RUN rm -rf build hyperbola MANIFEST.in README.md setup.py setup.cfg
