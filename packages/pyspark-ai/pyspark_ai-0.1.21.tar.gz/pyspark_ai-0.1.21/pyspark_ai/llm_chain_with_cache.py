from typing import Any, List, Optional

from langchain.chains import LLMChain
from langchain.callbacks.manager import Callbacks

from pyspark_ai.cache import Cache
from pyspark_ai.temp_view_utils import canonize_string

SKIP_CACHE_TAGS = ["SKIP_CACHE"]


class LLMChainWithCache(LLMChain):
    cache: Cache

    def run(
        self,
        *args: Any,
        callbacks: Callbacks = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> str:
        assert not args, "The chain expected no arguments"
        prompt_str = canonize_string(self.prompt.format_prompt(**kwargs).to_string())
        use_cache = tags != SKIP_CACHE_TAGS
        cached_result = self.cache.lookup(prompt_str) if use_cache else None
        if cached_result is not None:
            return cached_result
        result = super().run(*args, callbacks=callbacks, tags=tags, **kwargs)
        if use_cache:
            self.cache.update(prompt_str, result)
        return result
