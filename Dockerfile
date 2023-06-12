FROM python:3.11.4-alpine3.18
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt &&  \
    pip uninstall pip --yes && \
    rm -rf /root/.cache/pip
COPY . /app
CMD ["uvicorn", "text_app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]