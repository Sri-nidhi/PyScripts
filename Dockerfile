FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN  mkdir /src
COPY /Web_Scraping /src
CMD ["python","/src/Prt.py"]
