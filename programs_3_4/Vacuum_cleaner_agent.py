def vacuum_agent(location, status_A, status_B):
    if location == 'A' and status_A == 'Dirty':
        return 'SUCK'
    elif location == 'B' and status_B == 'Dirty':
        return 'SUCK'
    elif status_A == 'Dirty':
        return 'LEFT'
    elif status_B == 'Dirty':
        return 'RIGHT'
    else:
        return 'NO-OP'


def vacuum_simulation(location, status_A, status_B):
    print(f"\nInitial State: Location = {location}, Room A = {status_A}, Room B = {status_B}\n")
    
    while True:
        action = vacuum_agent(location, status_A, status_B)
        
        if action == 'NO-OP':
            print(f"Action: {action:<6} | Current State: Location = {location}, Room A = {status_A}, Room B = {status_B}")
            break
        
        if action == 'SUCK' and location == 'A':
            status_A = 'Clean'
        elif action == 'SUCK' and location == 'B':
            status_B = 'Clean'
        elif action == 'LEFT':
            location = 'A'
        elif action == 'RIGHT':
            location = 'B'
            
        print(f"Action: {action:<6} | Current State: Location = {location}, Room A = {status_A}, Room B = {status_B}")
        
    print(f"\nFinal State: Location = {location}, Room A = {status_A}, Room B = {status_B}")


def main():
    location = input("Enter Initial Location (A/B): ").strip().upper()
    status_A = input("Enter Status of Room A (Clean/Dirty): ").strip().capitalize()
    status_B = input("Enter Status of Room B (Clean/Dirty): ").strip().capitalize()
    
    vacuum_simulation(location, status_A, status_B)


if __name__ == "__main__":
    main()