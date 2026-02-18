def person_lister(func):
    """Decorator that sorts people by age and formats the output."""
    def wrapper(people):
        # Sort people by age (third element in tuple)
        sorted_people = sorted(people, key=lambda x: int(x[2]))
        
        # Format and return results
        result = []
        for person in sorted_people:
            formatted = f"{func(person)}"
            result.append(formatted)
        
        return '\n'.join(result)
    
    return wrapper


@person_lister
def display_person(person):
    """Format person info: first_name last_name (age, sex)"""
    first_name, last_name, age, sex = person
    return f"{first_name} {last_name}: {age}, {sex}"


# Example usage
if __name__ == "__main__":
    # Sample data: (first_name, last_name, age, sex)
    people = [
        ("John", "Smith", "30", "M"),
        ("Alice", "Johnson", "25", "F"),
        ("Bob", "Williams", "35", "M"),
        ("Diana", "Brown", "28", "F"),
        ("Charlie", "Davis", "22", "M"),
    ]
    
    print("Directory sorted by age:")
    print(display_person(people))