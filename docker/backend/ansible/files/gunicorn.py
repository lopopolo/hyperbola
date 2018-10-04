import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() + 1
accesslog = "-"
errorlog = "-"
capture_output = True
