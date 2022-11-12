import java.util.Scanner;
class nth
{
	public static void main(String arg[])
	{
		int i,n,temp;
		Scanner s=new Scanner(System.in);
		n=s.nectInt();
		Float avg,unit,ten,hud;
		unit=n%10;
		ten=(n/10)%10;
		hud=(n/100)%10;
		avg=(unit+ten+hud)/3;
	System.out.println(avg);
	}	
}