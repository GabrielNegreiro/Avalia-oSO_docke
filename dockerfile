# imagem base python
FROM python:3.11-slim

# define o diretório dentro do container
WORKDIR /app

# copia os arquivos de dependências
COPY requirements.txt .

# instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# copia o código do projeto para dentro do container
COPY . .

# expõe a porta do Django
EXPOSE 8000

# comando para rodar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

