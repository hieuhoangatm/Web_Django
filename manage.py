#!/usr/bin/env python
import os # mô-đun này cung cấp các chức năng để làm việc với hệ thống tệp và biến môi trường trong Python.
import sys #mô-đun này cho phép truy cập và tương tác với các thành phần của hệ thống Python, chẳng hạn như các tham số dòng lệnh và biến môi trường.

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
