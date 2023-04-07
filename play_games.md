---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

Notebook to play games of chance!

```python
import games
from matplotlib import pyplot as plt
```

The first game is flipping a coin. It will tell us either 'heads' or 'tails':

```python
games.flip_a_coin()
```

Next up is rolling a die. Let's make sure it isn't biased by plotting a histogram of many rolls:

```python
rolls = [games.roll_a_die(6) for i in range(1000)]
plt.hist(rolls, bins=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
```

Finally, we can pick a random card, which gives us two numbers that we can interpret as value and suit:

```python
games.pick_a_card()
```
