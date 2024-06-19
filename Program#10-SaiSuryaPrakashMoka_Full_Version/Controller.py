from RedBlackTree import *
if __name__ == "__main__":
    rbt = RedBlackTree()
    
    # Allow user to input text file to load
    file_path = input("Enter the path of the text file: ")
    
    # Load and decompose text
    text = rbt.load_text_file(file_path)
    words = rbt.decompose_text(text)
    
    # Add words to the tree
    for word in words:
        rbt.add_word(word)
    
    # Find a word in the tree
    search_word = input("Enter a word to find its occurrences: ")
    occurrences = rbt.find_word(search_word)
    print(f"'{search_word}' occurs {occurrences} time(s).")
    
    # Gather stats on the tree
    stats = rbt.gather_stats()
    print("Tree statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Save the tree to a file
    save_path = input("Enter the path to save the tree (JSON format): ")
    rbt.save_tree(save_path)
    
    # Remove a word from the tree
    remove_word = input("Enter a word to remove from the tree: ")
    rbt.delete_node(remove_word)
    print(f"'{remove_word}' has been removed from the tree.")
