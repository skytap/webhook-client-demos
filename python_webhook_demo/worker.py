# Copyright 2019 Skytap Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import atexit
import redis
from apscheduler.schedulers.background import BackgroundScheduler
from rq import Worker, Queue, Connection, get_failed_queue


class StartWorker(object):
    """This class handles the task queues and worker"""
    def __init__(self):
        self.redis_url = os.getenv('REDISTOGO_URL', 'redis:#localhost:6379')
        self.conn = redis.from_url(self.redis_url)
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
        """This method instantiate the rq worker"""
        with Connection(self.conn):
            worker = Worker(list(map(Queue, self.listen)))
            worker.work()
        return None

    def empty_queue(self):
        """This method clears out the previous failed queue.""""
        return self.failed_queue.empty()

    def retry_failed_queue(self):
        """This method retries failed jobs frome the failed queue."""
        for job_id in self.failed_queue.job_ids:
            self.failed_queue.requeue(job_id)
        return None

    def enqueue(self, func, args):
        """This method pushes a reference to the function 
        and its arguments onto a queue.
        
        Args: 
            func: The function performing the task. 
            args: The arguments the task function requires.
        """
        self.queue.enqueue_call(func=func,
                                args=args,
                                result_ttl=500)
        return None

    def run(self):
        """Start Redis""""
        self.empty_queue()
        self.start_worker()
        self.start_scheduler()
        return None


atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    sw = StartWorker()
    sw.run()
    atexit.register(lambda: sw.scheduler.shutdown())

