FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8501
CMD [ "streamlit", "run", "app.py"]
