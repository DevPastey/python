
def hanoi_solver(n):
    # Initialize rods: A has all disks (largest at bottom), others empty
    # We use lists as stacks where the last element is the top disk
    rods = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    
    # List to store the string representation of each state
    states = []

    def record_state():
        """Helper to capture the current arrangement of all rods."""
        # Convert lists to strings and join them with spaces
        state_str = f"{rods['A']} {rods['B']} {rods['C']}"
        states.append(state_str)

    def move_logic(disks, source, target, auxiliary):
        """Recursive core to move disks between rods."""
        if disks > 0:
            # Step 1: Move n-1 disks to the auxiliary rod
            move_logic(disks - 1, source, auxiliary, target)

            # Step 2: Move the nth disk to the target rod
            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()

            # Step 3: Move n-1 disks from auxiliary to the target rod
            move_logic(disks - 1, auxiliary, target, source)

    # 1. Capture the starting arrangement
    record_state()
    
    # 2. Run the solver (moving from A to C using B as helper)
    move_logic(n, 'A', 'C', 'B')

    # 3. Return all states joined by newlines
    return "\n".join(states)

# Example usage:
print(hanoi_solver(3))



