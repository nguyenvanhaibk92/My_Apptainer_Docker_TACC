FROM python:3.10

RUN pip install flask requests pyyaml redis

COPY app.py /app.py

CMD ["python", "app.py"]

# Build the image

# docker build -t nguyenvanhaibk92/coe332:0.0 .
# docker run -it --rm -p 5000:5000 nguyenvanhaibk92/coe332:0.0
# docker run -it --rm -p 5000:5000 -v /Users/vanhainguyen/Desktop/Github_Clone/test_git/Unit5_Containerization_and_Automation/docker/config.yaml:/config.yaml --rm nguyenvanhaibk92/coe332:0.0





