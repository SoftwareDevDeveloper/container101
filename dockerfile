From alpine:3.7

RUN apk update && \
    apk add python python3 && \
    pip3 install flask  && \
    mkdir -p /workspace

COPY app.py /workspace
WORKDIR /workspace

CMD ["flask", "run",  "--host=0.0.0.0", "--port=5000" ]