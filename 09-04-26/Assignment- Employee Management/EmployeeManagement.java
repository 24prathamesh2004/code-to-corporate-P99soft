import java.util.*;

public class EmployeeManagement {
    static ArrayList<Employee> employees = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n--- Employee Management System ---");
            System.out.println("1. Add Employee");
            System.out.println("2. View Employees");
            System.out.println("3. Update Employee");
            System.out.println("4. Delete Employee");
            System.out.println("5. Exit");

            System.out.print("Enter choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1: addEmployee(); break;
                case 2: viewEmployees(); break;
                case 3: updateEmployee(); break;
                case 4: deleteEmployee(); break;
                case 5: System.exit(0);
                default: System.out.println("Invalid choice!");
            }
        }
    }

    // Add Employee
    static void addEmployee() {
        System.out.print("Enter ID: ");
        int id = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Salary: ");
        double salary = sc.nextDouble();

        employees.add(new Employee(id, name, salary));
        System.out.println("Employee Added Successfully!");
    }

    // View Employees
    static void viewEmployees() {
        if (employees.isEmpty()) {
            System.out.println("No employees found!");
            return;
        }

        for (Employee e : employees) {
            e.display();
        }
    }

    // Update Employee
    static void updateEmployee() {
        System.out.print("Enter Employee ID to update: ");
        int id = sc.nextInt();
        sc.nextLine();

        for (Employee e : employees) {
            if (e.getId() == id) {
                System.out.print("Enter new Name: ");
                String name = sc.nextLine();

                System.out.print("Enter new Salary: ");
                double salary = sc.nextDouble();

                e.setName(name);
                e.setSalary(salary);

                System.out.println("Employee Updated Successfully!");
                return;
            }
        }
        System.out.println("Employee not found!");
    }

    // Delete Employee
    static void deleteEmployee() {
        System.out.print("Enter Employee ID to delete: ");
        int id = sc.nextInt();

        Iterator<Employee> it = employees.iterator();

        while (it.hasNext()) {
            Employee e = it.next();
            if (e.getId() == id) {
                it.remove();
                System.out.println("Employee Deleted Successfully!");
                return;
            }
        }
        System.out.println("Employee not found!");
    }
}