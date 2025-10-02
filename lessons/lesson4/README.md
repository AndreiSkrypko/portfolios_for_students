# Урок 4: Создание проектов - Собираем все вместе

## 📚 Цель урока
Научить детей создавать полноценные веб-проекты, объединяя HTML, CSS и JavaScript.

## ⏰ Время урока: 60 минут

## 🎯 Задачи урока
- Понять, как объединить все изученные технологии
- Создать полноценный проект
- Научиться планировать и структурировать код
- Познакомиться с реальными проектами

## 📋 План урока

### 1. Повторение и планирование (10 минут)
**Что рассказываем детям:**
- HTML создает структуру (скелет)
- CSS/Bootstrap делает красиво (одежда)
- JavaScript делает интерактивно (оживляет)

**Планирование проекта:**
- Обсуждаем, какой проект хотим создать
- Рисуем схему на доске
- Делим на этапы

**Вопросы для детей:**
- "Что мы изучили за предыдущие уроки?"
- "Какой проект вы хотели бы создать?"

### 2. Создание простого калькулятора (20 минут)
**Пошаговое создание:**

#### Шаг 1: HTML структура
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Мой калькулятор</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h1 class="text-center">Мой калькулятор</h1>
        <div class="row justify-content-center">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <input type="text" id="display" class="form-control mb-3 text-end" readonly>
                        <div class="row g-2">
                            <div class="col-3"><button class="btn btn-secondary w-100" onclick="clearDisplay()">C</button></div>
                            <div class="col-3"><button class="btn btn-secondary w-100" onclick="deleteLast()">⌫</button></div>
                            <div class="col-3"><button class="btn btn-warning w-100" onclick="appendToDisplay('/')">/</button></div>
                            <div class="col-3"><button class="btn btn-warning w-100" onclick="appendToDisplay('*')">×</button></div>
                        </div>
                        <!-- Добавляем остальные кнопки... -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

#### Шаг 2: JavaScript логика
```javascript
let display = document.getElementById('display');
let currentInput = '0';

function updateDisplay() {
    display.value = currentInput;
}

function appendToDisplay(value) {
    if (currentInput === '0' && value !== '.') {
        currentInput = value;
    } else {
        currentInput += value;
    }
    updateDisplay();
}

function clearDisplay() {
    currentInput = '0';
    updateDisplay();
}

function calculate() {
    try {
        currentInput = eval(currentInput).toString();
        updateDisplay();
    } catch (error) {
        currentInput = 'Ошибка';
        updateDisplay();
    }
}
```

**Практическое задание:**
- Дети создают калькулятор пошагово
- Тестируют каждую функцию
- Добавляют свои улучшения

### 3. Создание игры "Угадай число" (20 минут)
**Создаем игру с нуля:**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Угадай число</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body text-center">
                        <h1>🎯 Угадай число</h1>
                        <p>Я загадал число от 1 до 100. Попробуйте угадать!</p>
                        <p>Попыток: <span id="attempts">0</span></p>
                        <input type="number" id="guess" class="form-control mb-3" placeholder="Ваше число">
                        <button class="btn btn-primary" onclick="makeGuess()">Угадать</button>
                        <button class="btn btn-secondary" onclick="newGame()">Новая игра</button>
                        <p id="message" class="mt-3"></p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        let secretNumber = Math.floor(Math.random() * 100) + 1;
        let attempts = 0;

        function makeGuess() {
            const guess = parseInt(document.getElementById('guess').value);
            const message = document.getElementById('message');
            attempts++;

            if (guess === secretNumber) {
                message.innerHTML = `🎉 Поздравляем! Вы угадали за ${attempts} попыток!`;
                message.className = 'mt-3 text-success';
            } else if (guess < secretNumber) {
                message.innerHTML = '📈 Слишком мало!';
                message.className = 'mt-3 text-info';
            } else {
                message.innerHTML = '📉 Слишком много!';
                message.className = 'mt-3 text-info';
            }

            document.getElementById('attempts').textContent = attempts;
        }

        function newGame() {
            secretNumber = Math.floor(Math.random() * 100) + 1;
            attempts = 0;
            document.getElementById('guess').value = '';
            document.getElementById('message').innerHTML = '';
            document.getElementById('attempts').textContent = '0';
        }
    </script>
</body>
</html>
```

### 4. Создание портфолио (10 минут)
**Объединяем все в портфолио:**

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Мое портфолио</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="#">Мое портфолио</a>
        </div>
    </nav>

    <div class="container mt-5">
        <h1 class="text-center">Добро пожаловать в мое портфолио!</h1>
        
        <div class="row mt-5">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body text-center">
                        <h5>Калькулятор</h5>
                        <p>Простой калькулятор на JavaScript</p>
                        <a href="calculator.html" class="btn btn-primary">Посмотреть</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body text-center">
                        <h5>Угадай число</h5>
                        <p>Игра на угадывание числа</p>
                        <a href="guess-number.html" class="btn btn-success">Играть</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body text-center">
                        <h5>Обо мне</h5>
                        <p>Информация обо мне</p>
                        <a href="about.html" class="btn btn-info">Узнать больше</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

## 🎨 Домашнее задание
Создать свой собственный проект, объединяющий все изученные технологии.

## 🔧 Материалы для урока
- Готовые файлы из предыдущих уроков
- Примеры кода
- Схемы проектов

## ⚠️ Важные моменты
- Объясняем важность планирования
- Показываем, как тестировать код
- Учим структурировать файлы
- Поощряем творчество

## 🎯 Результат урока
Дети должны уметь:
- Планировать веб-проект
- Объединять HTML, CSS и JavaScript
- Создавать интерактивные элементы
- Структурировать код

## 📝 Дополнительные темы для любознательных
- Что такое файловая структура
- Как работает веб-сервер
- Основы отладки
- Планирование больших проектов

## 🎮 Интерактивные элементы урока
- Соревнование "Лучший проект"
- Демонстрация проектов друг другу
- Групповая работа над проектом

## 🏆 Критерии оценки проектов
- Работает ли код без ошибок
- Красиво ли выглядит
- Есть ли интерактивность
- Понятен ли код
- Креативность решения
