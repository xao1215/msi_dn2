FROM python
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip && \
    pip install --no-cache-dir flask redis pymongo
CMD python app.py
