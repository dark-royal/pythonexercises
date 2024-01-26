import java.util.Scanner;

public class BarChart1{

public static void main(String[] args){

Scanner scanner = new Scanner(System.in);

System.out.println("Enter number: ");
int number = scanner.nextInt();

if(number >= 1 && number <= 30){

	for(int count = number ; count <= 5; count++
		System.out.println("Enter number: ");
		number = scanner.nextInt();
		System.out.print("*");
	}
	
	System.out.println();
}

else{
	System.out.println("Invalid input");
}


}

}