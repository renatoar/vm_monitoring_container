FROM python:3.7-alpine
ADD vm_monitoring_container.py /
CMD ["python", "vm_monitoring_container.py"]