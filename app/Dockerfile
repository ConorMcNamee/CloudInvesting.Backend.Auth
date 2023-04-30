FROM python:3.11.3-alpine
WORKDIR /app

RUN apk --update --upgrade add --no-cache gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev python3-dev libpq-dev

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000

COPY . .
CMD ["python", "app.py"]