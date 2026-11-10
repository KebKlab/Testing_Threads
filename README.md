# Chaotic Pizzeria
An academic project developed in Python to simulate a pizzeria using concurrent and parallel programming.

**Features and Concepts**

  **Threads:** Manage chefs and delivery workers.
	**Queues:** Handle communication and order distribution between different stages.
  
  **Semaphores:** Control access to the ovens, limiting the number of chefs working simultaneously.

  **Events:** Synchronize the production and delivery stages.
  
  **ProcessPoolExecutor:** Distribute CPU-intensive tasks across multiple processes.

**Project Setup**

## Requirements:

  Python 3.8 or later
  
  No external dependencies required (uses Python standard library).
  
  The project explores fundamental concepts of concurrency, parallelism, synchronization, and resource management in Python.

## Implementations

This project includes two different implementations to compare concurrency and parallelism in Python:

### 1. Threading (pizzeria_threads.py)

Uses Python threads to manage chefs and delivery workers. CPU-intensive tasks are executed within threads, making this implementation subject to the limitations imposed by the Global Interpreter Lock (GIL).

### 2. Multiprocessing (pizzeria_multiprocessing.py)

Uses a hybrid approach combining threads and processes. The ProcessPoolExecutor distributes CPU-intensive tasks across multiple processes, allowing parallel execution and reducing the impact of the GIL.

## Running the Implementations

**Threading:**
```bash
python pizzeria_threads.py
```

**Multiprocessing:**
```bash
python pizzeria_multiprocessing.py
```
