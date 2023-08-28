FROM python:3.11-slim-bookworm
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8501
CMD [ "streamlit", "run", "app.py"]
