FROM python:3.7-alpine
ADD vm_monitoring_container.py /
RUN pip install requests
RUN pip install pymongo
CMD ["python", "vm_monitoring_container.py"]