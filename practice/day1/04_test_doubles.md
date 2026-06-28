## Практика
Использование тестовых дублеров
  
**Задача:** Написать тесты на выигрыш/проигрыш, которые зависят от значения кубика
- Игрок сделал правильную ставку и выиграл
- Игрок сделал неправильную ставку и проиграл ставку
- Мокируем кубик
- Обращаем внимание на
   - Наименование теста
   - Структуру теста (AAA)
   - Лаконичность и выразительность теста
   - Понятность тестовых данных
   - Уместное использование Stub
  
**Ответ:**
  
[Код теста](/practice/day1/dices/tests/test_dices_game_stub.py)
  
Меняем RollDiceGame.play() на вызов Dice.roll() вместо рандома.
``` Python
    def play(self):
        winning_score = Dice.roll()
        for bet in self._bets:
            if bet['score'] == winning_score:
                bet['player'].win(bet['chips'] * 6)
```
  
**Комментарий:**
  
Используется https://docs.pytest.org/en/stable/how-to/monkeypatch.html для stub  

## Практика
Использовать test doubles в упражнении dices
  
**Задача:** Понять разницу между тестами на поведение и тестами на состояние

**Поведение**
  
- Game.Play() бросает кубик
- Game.Play() вызывает Player.Win() для всех игроков в игре, сделавших правильную ставку
- Game.Play() не вызывает Player.Win() для всех игроков в игре, сделавших неправильную ставку
  
**Состояние** 
  
- После Game.Play() игрок, сделавший правильную ставку, выиграл 6 ставок
- После Game.Play() все игроки, сделавшие правильные ставки, выиграли по 6 ставок каждый
- После Game.Play() игрок, сделавший неправильную ставку, проиграл ставку
- После Game.Play() все игроки, сделавшие неправильные ставки, проиграли свои ставки
  
**Ответ:**
  
[Код теста](/practice/day1/dices/tests/test_dices_game_mock.py)
  
Тест проверяет новый метод RollDiceGame.play_new_game():
``` Python
    def play_new_game(self):
        num_rolls = Dice.roll()
        if num_rolls > 0:
            winning_score = None
            
            for _ in range(num_rolls):
                winning_score = Dice.roll()
        
            for bet in self._bets:
                if bet['score'] == winning_score:
                    bet['player'].win(bet['chips'] * 6)
```
  
**Комментарий:**
  
Необходимо использовать pytest и установить дополнительно библиотеку pytest-mockito для измерения покрытия:
```
pip install pytest mockito pytest-mockito
```
или на Windows
```
py -m pip install pytest mockito pytest-mockito
```
