# python3.11のイメージをダウンロード
FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /src
RUN pip install uv

COPY pyproject.toml* uv.lock* ./

RUN if [ -f pyproject.toml ]; then uv sync --no-install-project; fi

ENTRYPOINT ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
