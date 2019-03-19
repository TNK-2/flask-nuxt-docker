FROM python:3.7-alpine3.8
ENV PORT '5000'
WORKDIR /app
COPY ./app /app
RUN chmod +x /app/migration.sh
RUN pip3 install -r requirements.txt
CMD ["python3","app.py"]
EXPOSE 5000
