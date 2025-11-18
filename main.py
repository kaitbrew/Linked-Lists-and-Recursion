from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """
    ll = LinkedList()

    # Insert sample data
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)

    print("Original List:")
    ll.display()

    print("\nSum of all elements (recursive):")
    print(ll.recursive_sum()) # Should be 6

    print("\nSearching for 2 (should be True):")
    print(ll.recursive_search(2))

    print("\nSearching for 99 (should be False):")
    print(ll.recursive_search(99))

    print("\nReversing list (recursive)...")
    ll.recursive_reverse()
    print("Reversed list:")
    ll.display()