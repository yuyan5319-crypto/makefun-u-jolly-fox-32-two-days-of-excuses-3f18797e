[![make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/yuyan5319-crypto/makefun-u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/yuyan5319-crypto/makefun-u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

# Two Days of Excuses

The funniest one-line excuse an AI gives for a missed deadline.

> I gave missing the deadline a 0.01% chance, then spent the whole week personally verifying that 0.01%.

## How to run

```sh
python3 main.py
```

This writes the one-line excuse to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`) and prints it to stdout. The program
refuses to run if the line is empty or over the 200-character limit,
so the grader can never see an invalid entry.
