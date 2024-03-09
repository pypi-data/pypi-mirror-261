import asyncio
from typing import Any, Callable, List

import nest_asyncio
from tqdm.asyncio import tqdm  # Import tqdm for progress bars

from easyrag.utils import in_jupyter_notebook


class AsyncRunner:
    """
    A class to run asynchronous tasks with a concurrency limit.
    Attributes:
        concurrency_limit (int): The maximum number of tasks to run concurrently.
        callable (Callable): The asynchronous function to be called for each task.

    Methods:
        bounded_call(sample): Calls the provided callable within the concurrency limit.
        async_run(data): Asynchronously runs tasks on a set of data.
        run(data): Synchronous wrapper to run asynchronous tasks on a set of data.
    """

    def __init__(self, concurrency_limit=8, callable: Callable = None):
        if in_jupyter_notebook():
            nest_asyncio.apply()

        self.sem = asyncio.Semaphore(concurrency_limit)
        self.callable = callable

    async def bounded_call(self, sample: Any):
        """
        Asynchronously calls the callable function within the concurrency limit.
        """
        async with self.sem:
            return await self.callable(sample)

    async def async_run(self, data: List[Any]):
        """
        Asynchronously executes tasks on a collection of data.
        Args:
            data: A collection of data samples to be processed by the callable.

        Returns:
            A list of results from processing each data sample.
        """
        tasks = [self.bounded_call(sample) for sample in data]
        results = []
        for task in tqdm.as_completed(tasks, total=len(tasks)):
            result = await task
            results.append(result)
        return results

    def run(self, data: List[Any]) -> List[Any]:
        """
        Runs the asynchronous task execution on a collection of data synchronously.
        Args:
            data: A collection of data samples to be processed by the callable.

        Returns:
            A list of results from the asynchronous execution of tasks on the data.
        """
        return asyncio.run(self.async_run(data))
