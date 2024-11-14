# Image Base
FROM python3

# Team that will mantain the project
LABEL maintainer="EasyGroupIT"

# Project Directory
WORKDIR /app

# Copy the run.py file
COPY ./app.py /app/app.py

# Package Install
COPY ./requirements.txt /app/requirements.txt

# Package Install
RUN pip intall -r requirements.txt

# Start app
CMD ["python", "app.py"]
