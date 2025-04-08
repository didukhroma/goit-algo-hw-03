def hanoi_tower(n):
    first_tower_initial_state = list(range(n, 0, -1))
   
    initial_state = {'A': [*first_tower_initial_state], 'B': [], 'C': []}
    print(f"Initial state: {initial_state}")

    def move_disk(start_tower, dest_tower):
        disk = initial_state[start_tower].pop()
        initial_state[dest_tower].append(disk)
        print(f"Move disk  from {start_tower} to {dest_tower}: {disk}")
        print(f"Current state: {initial_state}") 

    def solve_hanoi(n, start_tower, dest_tower, mid_tower):
        if n == 1:
            move_disk(start_tower, dest_tower)
        else:
            solve_hanoi(n - 1, start_tower, mid_tower, dest_tower)
            move_disk(start_tower, dest_tower)
            solve_hanoi(n - 1, mid_tower, dest_tower, start_tower)

    solve_hanoi(n, 'A', 'C', 'B')
    print(f"Final state: {initial_state}") 
  
hanoi_tower(3)