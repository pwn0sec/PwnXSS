FROM python:3.7-alpine

# Create the non-root user up front to save a little time on rebuilds.
RUN adduser --gecos '' --disabled-password app

COPY requirements.txt requirements.txt

# it is better to chain commands to reduce the number of created layers
RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# Switch to the user "app"
USER app
WORKDIR /home/app
COPY . . 

ENTRYPOINT ["python3", "pwnxss.py"]


