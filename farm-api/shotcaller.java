/*
 * this program takes in the weather code
 * and decides if that means rain or not
 * the codes that are rain are:
 * 200, 201, 202
 * 230, 231, 232
 * 3xx
 * 5xx
 *
 */
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class shotcaller
{
	public static void main(String args[]) throws FileNotFoundException 
	{
		
		File raincode = new File("/home/pi/Gardenbot/dsaGreenhouseProjectFall2022/testing-api/raincode.txt"); 
		Scanner scnr = new Scanner(raincode);
		int code = scnr.nextInt(); 

		if((code == 200) || (code == 201) || (code == 202) || (code == 230) || (code == 231) || (code == 232) || ((code >= 300) && (code < 400)) || ((code >= 500) && (code < 600))) 
		{
			System.out.println("rain");
		}
		else
		{
			System.out.println("nope");
		}
	}
}

