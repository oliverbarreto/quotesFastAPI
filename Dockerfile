FROM python:3.9.6-alpine

# Set work directory
WORKDIR /app
# ADD . /app

# Copy init files
COPY ./requirements.txt /app/requirements.txt
COPY ./api.py /app/api.py

RUN pip install -r requirements.txt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8383"]



