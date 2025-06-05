# 🎓 Student Marks Analyzer using NumPy

This project is a small simulation built with **NumPy** to manage and analyze student marks across different subjects. It demonstrates usage of `NumPy` arrays, slicing, indexing, aggregation, and statistical functions — a great practice for beginner to intermediate Python learners.

---

## 🔧 Features

- ✅ Random data generation for marks (30–100)  
- ✅ Displays total marks per student  
- ✅ Calculates average marks per subject  
- ✅ Finds subject-wise toppers  
- ✅ Identifies students who failed in any subject  
- ✅ Detects highest and lowest marks with roll and subject

---

## 📊 Subjects Used

- Physics  
- Chemistry  
- Math  
- Biology

---

## 📥 Input

```bash
How many students? : 5
```

The program will generate a table like this:

```
Full Student Data:

[['Student Roll' 'Physics' 'Chemistry' 'Math' 'Biology']
 ['Roll-1  '      81         94          74     75]
 ['Roll-2  '      57         87          30     91]
 ...
]
```

---

## 📈 Sample Output

```bash
Total Marks per Student:

Roll-1   → 324  
Roll-2   → 265  
...

Average Marks per Subject:
Physics   : 68.4  
Chemistry : 79.2  
Math      : 66.0  
Biology   : 72.6  

Topper in Each Subject:
Physics    → Roll-4   (94 marks)  
Chemistry  → Roll-3   (97 marks)  
Math       → Roll-5   (89 marks)  
Biology    → Roll-1   (91 marks)  

Students Who Failed in Any Subject:
Roll-2
Roll-5

Highest Mark: 97 → Roll-3   in Chemistry  
Lowest Mark : 30 → Roll-2   in Math
```

---

## 🧠 Concepts Covered

- Object arrays and slicing  
- Data type casting with `.astype()`  
- Random number generation with `np.random.randint()`  
- Aggregations with `np.sum()` and `np.mean()`  
- Indexing with `np.argmax()`, `np.any()`, `np.unravel_index()`  
- Conditional filtering

---

## 🚀 Getting Started

### Requirements

- Python 3.x  
- NumPy

### Run

```bash
python student_performance_tracker.py
```

---

## 📁 File Structure

```
student_performance_tracker.py     # Main script
README.md            # Project explanation (you are here)
```

---

## 📜 License

This project is open source and free to use. Learning is always welcome! ❤️

---

## 🙋‍♂️ Author

Made with ❤️ by [Md Mahmud Hassan Rafi] 
Still learning NumPy — one array at a time!
