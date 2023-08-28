FROM python:3.7
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8501
CMD [ "streamlit", "run", "app.py"]