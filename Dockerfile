FROM python

WORKDIR /app/
COPY taskLister /app/taskLister
COPY tasksApp /app/tasksApp
COPY db.sqlite3 /app/db.sqlite3
COPY manage.py /app/manage.py

COPY requirements.txt /app/requirements.txt
ENV PYTHONUNBUFFERED=1
RUN pip3 install -r /app/requirements.txt

CMD [ "python3","manage.py", "runserver", "0.0.0.0:8000"]
