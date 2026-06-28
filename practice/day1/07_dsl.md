## Практика Game of Life
#### Правила игры жизнь 
  
- Игра происходит на клеточном поле - «вселенной».
- Каждая клетка может быть живой или мёртвой (пустой).
- Поколения сменяются синхронно по простым правилам:
   - в пустой клетке, рядом с которой ровно три живых, зарождается жизнь
   - если у живой клетки есть два или три живых соседа, то клетка продолжает жить
   - если соседей меньше двух или больше трёх, то клетка умирает «от одиночества» или «от перенаселённости»
   
#### Тесты
  
- Придумать, какие нужны тесты 
- Подумать, как могут выглядеть DSL-style тесты

**Ответ:**
  
Тесты:
- пустая игра остается пустой после следующего шага
``` Python
def test_empty_game_is_empty_in_next_generation():
    game = Create.game().please()
    game.next_generation()
    assert game == Game("")
```
- клетка выживает, если у нее два соседа
``` Python
def test_two_neighbors_cell_survives():
    game = Create.game(""" 
                       * . . 
                       . * .
                       . . *
                       """).please()
    game.next_generation()
    assert game == Game(""" 
                       . . . 
                       . * .
                       . . .
                       """)
```
- клетка выживает, если у нее три соседа
``` Python
def test_three_neighbors_cell_survives():
    game = Create.game(""" 
                       . . . .
                       . * * .
                       . * * .
                       . . . .
                       """).please()
    game.next_generation()
    assert game == Game(""" 
                       . . . .
                       . * * .
                       . * * .
                       . . . .
                       """)
```
- клетка рождается, если у нее три соседа
``` Python
def test_three_neighbors_cell_borns():
    game = Create.game(""" 
                       . * .
                       . * .
                       . * .
                       """).please()
    game.next_generation()
    assert game == Game(""" 
                       . . . 
                       * * * 
                       . . . 
                       """)
```


## Практика Dices

#### Тесты на Dice Roll Game
Напишите DSL тесты на Dice Roll Game.
  
**Примеры:**
  
- Create. подскажет какие сущности есть в вашем домене
- Create.Entity() создаст билдер 
- Create.Entity().with_smth().with_smth_else() подскажет как можно параметризовать сущность в билдере
- Create.Entity().please() вернет сущность из билдера

**Ответ:**

[Код теста](/practice/day1/dices/tests/test_dices_game_dsl.py)
