def simulate_movement(commands):
    positions = set()

    def move(cmds):
        pos, direction = 0, 1  # 0 - начальная позиция, 1 - направление вправо
        for cmd in cmds:
            if cmd == 'F':
                pos += direction
            elif cmd == 'L':
                direction = -1
            elif cmd == 'R':
                direction = 1
        return pos

    # Проверяем все возможные варианты исправления ошибки
    for i in range(len(commands)):
        # Создаем вариант последовательности без i-й команды
        new_commands = commands[:i] + commands[i+1:]
        positions.add(move(new_commands))
        
        # Создаем варианты последовательности, заменяя i-ю команду на каждую из возможных команд
        for cmd in 'FRL':
            if cmd != commands[i]:
                new_commands = commands[:i] + cmd + commands[i+1:]
                positions.add(move(new_commands))

    return len(positions)

# Считываем и проверяем входные данные
try:
    N = int(input())
    if not (1 <= N <= 3 * 10**5):
        raise ValueError("N должно быть в диапазоне от 1 до 3*10^5")
    
    commands = input().strip()
    if len(commands) != N:
        raise ValueError("Количество символов во второй строке должно быть равно N")
    
    if not all(cmd in 'FRL' for cmd in commands):
        raise ValueError("Строка команд должна содержать только символы F, R, L")

    # Вычисляем и выводим результат
    result = simulate_movement(commands)
    print(result)

except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")