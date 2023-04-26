FROM python:3.9.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
RUN python training.py
EXPOSE 3000
CMD python chatbot.py 