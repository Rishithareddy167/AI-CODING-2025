function printStudents(students) {
    console.log("Student List:");
    for (let i = 0; i < students.length; i++) {
        console.log("• " + students[i]);
    }
}

// Test the function
printStudents(["Alice", "Bob", "Charlie"]);