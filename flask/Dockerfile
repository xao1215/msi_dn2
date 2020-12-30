FROM python
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip && \
    pip install --no-cache-dir flask redis
CMD python app.py
