import java.util.Scanner;

public class LargestAndSmallest{

public static void main(String[] args){

Scanner scanner = new Scanner(System.in);

System.out.println("Enter number: ");
int number = scanner.nextInt();

int largest = 0;

int smallest = 0;

int count = 0;

while(number != -1){

	if(largest > number){

		largest = number;
}

	else{

		smallest = number;
}
	System.out.println("Enter number: ");
	int number = scanner.nextInt();

	count++;
}
	

}


}