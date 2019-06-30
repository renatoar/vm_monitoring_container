FROM python:3.7-alpine
ADD vm_monitoring_container.py /
RUN pip install requests
CMD ["python", "vm_monitoring_container.py"]