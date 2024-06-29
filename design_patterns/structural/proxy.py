"""
In this implementation, the CacheProxy serves as an intermediary
between the client and the RealDatabaseQuery.
It checks whether the result of a query is already cached and,
if so, returns the cached result within the specified cache duration.

If the result is not in the cache or has expired, it delegates the
query execution to the RealDatabaseQuery, caches the result,
and returns it to the client. This way, the CacheProxy reduces
the load on the database server and speeds up data retrieval by
serving cached results when possible.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
import time


# define the interface for the real object
class IDatabaseQuery(ABC):
    @abstractmethod
    def execute_query(self, query):
        pass


# real subject: represents the actual database
class RealDatabaseQuery(IDatabaseQuery):
    def execute_query(self, query):
        print(f"Executing query:\n{query}")
        # simulates database query and returns results
        return f"Results for query: {query}"


# proxy: caching proxy for database queries
class CacheProxy(IDatabaseQuery):
    def __init__(self, real_database_query, cache_duration):
        self._real_database_query = real_database_query
        self._cache = {}
        self._cache_duration = cache_duration  # seconds

    def execute_query(self, query):
        if (query in self._cache) and (
            time.time() - self._cache[query]["timestamp"] <= self._cache_duration
        ):
            # Return cached results
            print(
                f"CachedProxy: Returning result for{query}",
                f", time: {self._cache[query]['timestamp']}",
            )
            return self._cache[query]
        else:
            # execute wquery and cache the result
            result = self._real_database_query.execute_query(time.time())
            self._cache[query] = {"result": result, "timestamp": time.time()}
            return result


if __name__ == "__main__":
    real_db_query = RealDatabaseQuery()
    cached_query = CacheProxy(
        real_database_query=real_db_query, cache_duration=0.000005
    )

    for i in range(100):
        res = cached_query.execute_query("query 1")
        # print(res)
