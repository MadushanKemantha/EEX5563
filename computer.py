import tkinter as tk
from tkinter import messagebox

def first_fit(memory_blocks, process_sizes):
    """
    Simulate the First Fit memory allocation.
    Allocate the first suitable memory block to each process.
    """
    allocation = [-1] * len(process_sizes)  # Store allocated block index (-1 if unallocated)

    for i in range(len(process_sizes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= process_sizes[i]:  # Check if block fits
                allocation[i] = j  # Allocate block
                memory_blocks[j] -= process_sizes[i]  # Update block size
                break

    return allocation

class FirstFitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("First Fit Memory Allocation")
        self.root.configure(bg="#f0f8ff")  # Light blue background

        self.memory_blocks = []
        self.process_sizes = []

        # Memory Block Section
        tk.Label(root, text="Memory Blocks (Sizes)", bg="#f0f8ff", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.memory_entry = tk.Entry(root, width=20)
        self.memory_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(root, text="Add Block", command=self.add_memory_block, bg="#add8e6").grid(row=0, column=2, padx=10, pady=5)

        # Process Size Section
        tk.Label(root, text="Process Sizes", bg="#f0f8ff", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.process_entry = tk.Entry(root, width=20)
        self.process_entry.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(root, text="Add Process", command=self.add_process, bg="#add8e6").grid(row=1, column=2, padx=10, pady=5)

        # Run Button
        tk.Button(root, text="Run First Fit", command=self.run_first_fit, bg="#4682b4", fg="white", font=("Arial", 12)).grid(row=2, column=0, columnspan=3, pady=10)

        # Result Display
        self.result_text = tk.Text(root, height=15, width=50, state=tk.NORMAL, bg="#f8f9fa", font=("Courier", 10))
        self.result_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Show initial data
        self.update_display()

    def update_display(self):
        """Show memory blocks and processes."""
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)

        self.result_text.insert(tk.END, "Memory Blocks: " + ", ".join(map(str, self.memory_blocks)) + "\n")
        self.result_text.insert(tk.END, "Processes: " + ", ".join(map(str, self.process_sizes)) + "\n\n")

    def add_memory_block(self):
        """Add a memory block."""
        try:
            size = int(self.memory_entry.get())
            self.memory_blocks.append(size)
            self.memory_entry.delete(0, tk.END)
            self.update_display()
            messagebox.showinfo("Success", f"Added Memory Block of size {size}")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number for memory block size.")

    def add_process(self):
        """Add a process."""
        try:
            size = int(self.process_entry.get())
            self.process_sizes.append(size)
            self.process_entry.delete(0, tk.END)
            self.update_display()
            messagebox.showinfo("Success", f"Added Process of size {size}")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number for process size.")

    def run_first_fit(self):
        """Run the First Fit algorithm and display results."""
        if not self.memory_blocks:
            messagebox.showerror("Error", "Add memory blocks first.")
            return
        if not self.process_sizes:
            messagebox.showerror("Error", "Add processes first.")
            return

        # Avoid changing the original memory block list
        memory_blocks_copy = self.memory_blocks[:]
        allocation = first_fit(memory_blocks_copy, self.process_sizes)

        # Display results
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)

        self.result_text.insert(tk.END, "Process No.\tProcess Size\tBlock Allocated\n")
        for i, process_size in enumerate(self.process_sizes):
            block_allocated = allocation[i] + 1 if allocation[i] != -1 else "Not Allocated"
            self.result_text.insert(tk.END, f"{i + 1}\t\t{process_size}\t\t{block_allocated}\n")

        self.result_text.configure(state=tk.DISABLED)

# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FirstFitApp(root)
    root.mainloop()
