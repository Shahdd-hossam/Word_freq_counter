FROM python
WORKDIR /app
COPY . /app
COPY paragraphs.txt /app/
RUN pip install nltk 
CMD ["python" , "script.py"]

