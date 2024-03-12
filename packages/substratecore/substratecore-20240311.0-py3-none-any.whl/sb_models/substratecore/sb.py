from typing import Union

from sb_models.substratecore.base_future import Concatable, ConcatDirective
from sb_models.substratecore.client.future import Future

StringConcatable = Union[str, Future]


class sb:
    @classmethod
    def concat(cls, *args: StringConcatable) -> StringConcatable:
        if len(args) == 0:
            return ""
        elif len(args) == 1:
            return args[0]
        else:
            concat_args = []
            futures = []
            for arg in args:
                is_future = isinstance(arg, Future)
                if is_future:
                    futures.append(arg)
                concat_args.append(
                    Concatable(
                        future_id=arg.id if is_future else None,
                        val=arg if not is_future else None,
                    )
                )

            directive = ConcatDirective(type="string-concat", items=concat_args)
            os = Future(directive=directive)
            # draw edges from the concat op to all of its child futures
            for f in futures:
                os.FutureG.add_edge(f, os)
            return os
