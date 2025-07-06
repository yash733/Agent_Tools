FROM python:3.9

WORKDIR /Chat_with_search

COPY . /Chat_with_search

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit","run","src/main.py"]
