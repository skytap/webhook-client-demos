import os
import atexit
import redis
from apscheduler.schedulers.background import BackgroundScheduler
from rq import Worker, Queue, Connection, get_failed_queue


class StartWorker(object):
    def __init__(self):
        self.redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
        self.conn = redis.from_url(redis_url)
        self.queue = Queue(connection=self.conn)
        self.listen = ['default']
        self.failed_queue = get_failed_queue(connection=self.conn)
        self.scheduler = BackgroundScheduler()

        return None

    def start_scheduler(self):
        self.scheduler.add_job(func=self.retry_failed_queue,
                               trigger="interval", seconds=30)
        self.scheduler.start()
        return None

    def start_worker(self):
        with Connection(self.conn):
            worker = Worker(list(map(Queue, self.listen)))
            worker.work()
        return None

    def empty_queue(self):
        return self.failed_queue.empty()

    def retry_failed_queue(self):
        for job_id in self.failed_queue.job_ids:
            self.failed_queue.requeue(job_id)
        return None

    def enqueue(self, func, args):
        self.queue.enqueue_call(func=func,
                                args=args,
                                result_ttl=500)
        return None
    def run(self):
        self.empty_queue()
        self.start_worker()
        self.start_scheduler()
        return None


atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    sw = StartWorker()
    sw.run()
    atexit.register(lambda: sw.scheduler.shutdown())

