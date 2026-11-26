# Warning Label for Humans: One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![make.fun rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/oliversmith74928-oss/mini-warning-label-humans-20261126/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![make.fun reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/oliversmith74928-oss/mini-warning-label-humans-20261126/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the [make.fun bounty "Warning Label for Humans: One Line, Big Laugh"](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85).

`main.py` (Python standard library only) writes one line — the funniest safety
warning label that should come printed on every human being, 160 characters
or fewer — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

The label:

> WARNING: This human will spend twenty minutes choosing what to watch, fall asleep ten minutes in, and wake up asking what happened.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The output is byte-identical across runs.
