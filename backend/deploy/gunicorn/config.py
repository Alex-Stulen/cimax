import multiprocessing

# адрес и порт, на которых будет запущен gunicorn
bind = '0.0.0.0:8000'

# количество воркеров gunicorn
workers = multiprocessing.cpu_count() * 2 + 1

# максимальное количество запросов, которые может обработать каждый воркер до перезапуска
max_requests = 1000

# максимальное количество запросов, которые может обработать воркер до того, как он будет перезагружен
max_requests_jitter = 50

timeout = 3600
client_max_body_size = '100G'
