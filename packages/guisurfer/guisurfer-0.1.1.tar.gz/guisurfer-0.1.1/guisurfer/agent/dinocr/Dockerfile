FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN git clone https://github.com/X-PLUG/MobileAgent ./MobileAgentRepo

RUN pip install -r ./MobileAgentRepo/requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app:/app/MobileAgentRepo"

CMD ["python", "-m", "guisurfer.agents.gpt4v_aug.main"]
