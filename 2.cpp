# include <iostream> 
using namespace std;

/* Suppose John and Bill worked for some time and need to calculte the total time both worked
Write a program that reads number of days, hours, minutes each of them worked, and prints the total time both of them
worked together as days, hours, minutes
The expected output is given as 6 days, 3 hours, 35 minutes

 */

int main() {
    const int HOURS = 24; 
    const int DAY = 1;
    
    int daysJohn;
    int hoursJohn;
    int minutesJohn;

    int daysBill;
    int hoursBill;
    int minutesBill;

    cout << "Please enter the number of days John worked: \n";
    cin >> daysJohn; 
    cout << "Please enter the number of hours John worked: \n";
    cin >> hoursJohn; 
    cout << "Please enter the number of minutes John worked: \n";
    cin >> minutesJohn; 

    cout << "Please enter the number of days Bill worked: \n";
    cin >> daysBill; 
    cout << "Please enter the number of hours Bill worked: \n";
    cin >> hoursBill; 
    cout << "Please enter the number of minutes Bill worked: \n";
    cin >> minutesBill;

    
    int totalMinutes = minutesJohn + minutesBill;  // 35 minutes
    int totalHours = (hoursBill + hoursJohn) - HOURS; // 27 hours - 24 hours (day) == 3
    int totalDays = daysJohn + daysBill + DAY; // 2 + 3 + 1 manually carried the day over since I knew I had 24 hours left over (27-24)


    cout << "The total time both of them worked together is: " << totalDays << "days, " << totalHours << "hours, " << totalMinutes << "minutes";








}
