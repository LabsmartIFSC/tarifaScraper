FROM python:3.6.3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p code/output
COPY ./code/* ./code/
CMD ["python", "/usr/src/app/code/run.py"]
