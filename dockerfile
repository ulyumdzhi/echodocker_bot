FROM python:3.8-slim
ENV TOKEN='your_token'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]
