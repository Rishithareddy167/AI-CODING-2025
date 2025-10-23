class Car {
    constructor(brand, model, year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    displayDetails() {
        console.log("Car Details:");
        console.log("• Brand:", this.brand);
        console.log("• Model:", this.model);
        console.log("• Year:", this.year);
    }
}

// Create and test the object
const car1 = new Car("Toyota", "Corolla", 2020);
car1.displayDetails();