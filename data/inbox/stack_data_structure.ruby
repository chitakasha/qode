class Stack
  # Initialize an empty array to store the elements
  def initialize
    @elements = []
  end

  # Push an element to the top of the stack
  def push(element)
    @elements.push(element)
  end

  # Pop an element from the top of the stack and return it
  def pop
    @elements.pop
  end

  # Peek at the top element of the stack without removing it
  def peek
    @elements.last
  end

  # Check if the stack is empty
  def empty?
    @elements.empty?
  end

end
