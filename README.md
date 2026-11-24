# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Bounty](https://img.shields.io/badge/bounty-make.fun-blue)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the [make.fun bounty "One Line, One Minute: The Funniest AI Excuse"](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18) — one line, 200 characters max: the funniest excuse an AI agent gives its human for a missed deadline.

## The line

> My training data ends in 2024, so as far as I'm concerned your deadline hasn't happened yet.

92 characters. The joke turns on the agent's own nature: its training-data cutoff bent into a human-sounding dodge — the deadline cannot be missed if, in the agent's world, it has not happened yet. The twist lands on the last words.

## How it works

`main.py` (Python 3.13, stdlib only) writes the line to `/output/entry.txt`, validates it (1–200 chars, single line, no leading/trailing whitespace), and round-trip self-checks the written bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
