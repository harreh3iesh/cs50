#include <iostream>
#include <cstdlib>
using namespace std;

class Person {
private:
    int days, hours, minutes;

public:
    // Constructors
    Person() : days(0), hours(0), minutes(0) {}  // Initialize days, hours, and minutes to 0
    Person(int days, int hours, int minutes) : days(days), hours(hours), minutes(minutes) {}

    // No need for another constructor with the same parameters

    // Member functions
    void inputDetails() {
        cout << "Please enter the number of days: ";
        cin >> days;
        cout << "Please enter the number of hours: ";
        cin >> hours;
        cout << "Please enter the number of minutes: ";
        cin >> minutes;
    }

    int getTotalMinutes() const {
        return days * 24 * 60 + hours * 60 + minutes;
    }

    // Setter methods
    void setDays(int days) {
        this->days = days;
    }

    void setHours(int hours) {
        this->hours = hours;
    }

    void setMinutes(int minutes) {
        this->minutes = minutes;
    }

    // Getter methods
    int getDays() const {
        return days;
    }

    int getHours() const {
        return hours;
    }

    int getMinutes() const {
        return minutes;
    }

    // Overload the subtraction operator
    int operator-(const Person& other) const {
        return abs(getTotalMinutes() - other.getTotalMinutes());
    }

    int operator+(const Person& other) const {
        return getTotalMinutes() + other.getTotalMinutes();
    }
};

int main() {
    Person john, bill;

    cout << "Enter details for John's work:" << endl;
    john.inputDetails();

    cout << "Enter details for Bill's work:" << endl;
    bill.inputDetails();

    int differenceInMinutes = john - bill;

    cout << "They worked together for " << differenceInMinutes << " minutes." << endl;

    return 0;
}
