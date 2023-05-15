import math

def compute_distance(movements):
    x = 0
    y = 0
    
    for i in range(0, len(movements), 2):
        direction = movements[i]
        steps = int(movements[i+1])
        
        if direction == 'UP':
            y += steps
        elif direction == 'DOWN':
            y -= steps
        elif direction == 'LEFT':
            x -= steps
        elif direction == 'RIGHT':
            x += steps
    
    distance = math.sqrt(x**2 + y**2)
    return round(distance)

# Example usage
movements = ['UP', '5', 'DOWN', '3', 'LEFT', '3', 'RIGHT', '2']
distance = compute_distance(movements)
print(distance)
