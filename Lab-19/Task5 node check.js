public class Car {
    String brand;
    String model;
    int year;

    // Constructor
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    // Method to display details
    public void displayDetails() {
        System.out.println("Car Details:");
        System.out.println("• Brand: " + brand);
        System.out.println("• Model: " + model);
        System.out.println("• Year: " + year);
    }

    // Main method to test
    public static void main(String[] args) {
        Car car1 = new Car("Toyota", "Corolla", 2020);
        car1.displayDetails();
    }
}