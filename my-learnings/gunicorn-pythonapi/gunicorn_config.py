# gunicorn_config.py

bind = "0.0.0.0:5000"
workers = 4
timeout = 2  # Workers timeout after 30 seconds
loglevel = "info"
accesslog = "/home/utsav/Desktop/Personal_git/gunicorn-pythonapi/access_log/access.log"
errorlog = "/home/utsav/Desktop/Personal_git/gunicorn-pythonapi/error_log/error.log"
max_requests = 1000  # Restart workers after serving 1000 requests
preload_app = True  # Preload app before forking workers
graceful_timeout = 30  # Graceful worker shutdown timeout
keepalive = 2  # Keep connections alive for 2 seconds
#daemon = True  # Run in background
