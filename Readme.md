### Examples:

__inception.json__
```python3 ft_turing.py machines/inception.json '<alphabet=["1", ".", "+", "="]><states=["move_to_plus", "move_to_equal", "end", "HALT"]><transitions={"move_to_plus":[{"read":"1", "to_state":"move_to_plus", "write":"1", "action":"RIGHT"}, {"read":"0", "to_state":"move_to_plus", "write":"0", "action":"RIGHT"}, {"read":"+", "to_state":"move_to_equal", "write":"1", "action":"RIGHT"}], "move_to_equal":[{"read":"1", "to_state":"move_to_equal", "write":"1", "action":"RIGHT"}, {"read":"0", "to_state":"move_to_equal", "write":"0", "action":"RIGHT"}, {"read":"=", "to_state":"end", "write":".", "action":"LEFT"}], "end":[{"read":"1", "to_state":"HALT", "write":".", "action":"LEFT"}]}>1+1='```

__palindrome.json__
```python3 ft_turing.py machines/palindrome.json "1001001"```

__equal.json__
```python3 ft_turing.py machines/equal.json "000111"```

__is_pair.json__
```python3 ft_turing.py machines/is_pair.json "0000="```

__unary_add.json__

```python3 ft_turing.py machines/unary_add.json "111+11="```

__unary_sub.json__
```python3 ft_turing.py machines/unary_sub.json "111-11="```
